#!/usr/bin/env python3

# TODO:
#> Set up program arguments to:
#  - Automatically launch Chrome in a memory-limited cgroup
#  - Automatically launch Firefox in a memory-limited cgroup

# Global imports
import socket, sys, threading, time, subprocess, random, pickle, getopt, select

# Local imports
import svjesus.ffz

# Vanity banner
_vBanner = """
\t .d8888b.  888     888 888888
\td88P  Y88b 888     888   "88b
\tY88b.      888     888    888
\t "Y888b.   Y88b   d88P    888  .d88b.  .d8888b  888  888 .d8888b
\t    "Y88b.  Y88b d88P     888 d8P  Y8b 88K      888  888 88K
\t      "888   Y88o88P      888 88888888 "Y8888b. 888  888 "Y8888b.
\tY88b  d88P    Y888P       88P Y8b.          X88 Y88b 888      X88
\t "Y8888P"      Y8P        888  "Y8888   88888P'  "Y88888  88888P'
\t                        .d88P
\t                      .d88P"
\t                     888P"
"""

# Global variables
_count     = 0
_tCount    = 0
_randSeed  = 0
_jsMess    = open("mess.js", "r").read()
_fuzzPort  = 9999
_fuzzEvt   = threading.Event()
_fuzzHost  = "127.0.0.1"
_reloadStr = """\
<!doctype html>
<html><head><script>%s</script></head>
<body onload="jsMess(function(){document.location.reload();})">
<script>
var seed = Math.floor(Math.random() * 100);
</script>
""" % _jsMess
_closeStr  = """</body></html>"""
_httpResp  = """\
HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Content-Type: text/html; charset=utf-8
Content-Length: {}
Connection: close

{}"""
_sTimeout    = 10
_autoReload  = False
_pFuzzLen    = 20
_pFuzzIdx    = 0
_pFuzzes     = [None for _ in range(_pFuzzLen)]
_countThread = None
_fuzzThread  = None
_crashWait   = False



# Thread to count the number of requests/sec
def counter():
    global _count, _tCount

    while _fuzzEvt.is_set():
        time.sleep(1)
        print("Requests per second: %d                    " % _count, end="\r")
        _tCount += _count
        _count = 0

# HTTP socket handler thread
def webFuzz():
    global _count, _pFuzzes, _pFuzzIdx, _tCount
    print("Fuzzing on %s:%d..." % (_fuzzHost, _fuzzPort))

    # Who needs HTTP libraries anyway?
    while _fuzzEvt.is_set():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((_fuzzHost, _fuzzPort))
        s.settimeout(_sTimeout)
        s.listen(1)

        # Generate our fuzz data
        fuzzData = svjesus.ffz.genSVG().encode("UTF-8")

        # Store the fuzz data in the rolling backlog, in case we hit a crash
        # TODO: Is storing the most recent fuzz enough? Hmm.
        _pFuzzes[_pFuzzIdx] = fuzzData
        _pFuzzIdx = (_pFuzzIdx + 1) % _pFuzzLen

        # Get our response ready
        sendLen   = len(fuzzData)
        if _autoReload:
            sendLen  += len(_reloadStr.encode("UTF-8"))
            sendLen  += len(_closeStr.encode("UTF-8"))
        fullData  = _httpResp.format(sendLen,_reloadStr if _autoReload else "").encode("UTF-8")
        fullData += fuzzData
        fullData += _closeStr.encode("UTF-8") if _autoReload else b""

        try:
            # Wait for a connection
            con,adr = s.accept()
            # If we get a connection, the browser hasn't crashed
            _crashWait = False
        # If we don't get a connection within _sTimeout, assume a crash
        except Exception:
            if _fuzzEvt.is_set():
                # Assuming we're fuzzing, have sent a fuzz and aren't already waiting
                if _tCount != 0 and not _crashWait:
                    print("No requests after %d seconds! Crash?" % _sTimeout)
                    dumpLast()
                    _crashWait = True
                    continue
                else:
                    continue
            else:
                break

        # Read some of the request
        con.recv(1)

        # Send a HTTP response with our fuzz data
        con.send(fullData)
        _count += 1
        con.close()
        s.close()

# Thread to handle launching a browser and catching crashes
# def browserFuzz():
#     while _fuzzEvt.is_set():
#         # print("Fuzzing browser in memory-limited cgroup 'NEWFUZZ'...")
#         # chrom = subprocess.Popen(["/usr/bin/cgexec", "-g memory:NEWFUZZ chromium http://127.0.0.1:9999/"])
#         chrom = subprocess.Popen(["/usr/lib/chromium/chromium", "http://127.0.0.1:9999/"])
#         chromStat = chrom.poll()
#         while chromStat == None:
#             if _fuzzing:
#                 chromStat = chrom.poll()
#             else:
#                 chrom.kill()
#         print("Chrome died with signal: %d!" % abs(chromStat))

# Some people are silly
def usage():
    print("$ %s -p<>/--port=<> -s<>/--seed=<> -a/--autoreload" % sys.argv[0])

# Print fuzz status
def dumpStats():
    print("Served ~%d requests\n" % _tCount)

# Dump last _pFuzzLen fuzzes
def dumpLast():
    dumpFileName = "".join(chr(random.randint(65,90)) for _ in range(0,10))+".fpl"
    with open(dumpFileName, "wb") as dumpFile:
        pickle.dump(_pFuzzes, dumpFile)
    dumpStats()
    print("Dumped last %d fuzzes to '%s':\n" % (_pFuzzLen, dumpFileName))

# Join all threads
def cleanUp():
    global _countThread, _fuzzThread, _fuzzEvt
    _fuzzEvt.clear()

    try:    _countThread.join()
    except: pass

    try:   _fuzzThread.join()
    except: pass

# Main logic
def main(opts, args):
    global _fuzzPort, _randSeed, _autoReload, _fuzzEvt, _fuzzThread, _countThread
    
    # Set the random seed
    _randSeed = random.randint(100,10000)
    
    # Set options
    for o, a in opts:
        if o in ("-p", "--port"):
            _fuzzPort = int(a)
        elif o in ("-s", "--seed"):
            _randSeed = int(a)
        elif o in ("-a", "--autoreload"):
            _autoReload = True
        else:
            assert False, "Unknown option %s" % o
    print("Using random seed: %d" % _randSeed)
    print("Using port:        %d" % _fuzzPort)
    print("Autoreload is %sabled" % ("en" if _autoReload else "dis"))
    random.seed(_randSeed)

    # Set the fuzzing event
    _fuzzEvt.set()

    # Start threads
    _countThread = threading.Thread(target=counter)
    _countThread.start()
    _fuzzThread = threading.Thread(target=webFuzz)
    _fuzzThread.start()

    # Main loop; waiting for and acting on user input
    while True:
        cmd = ""
        if select.select([sys.stdin], [], [], 2)[0]:
            cmd = sys.stdin.readline().strip()
        else:
            continue

        # Q to quit
        if cmd in ("q", "Q"):
            dumpStats()
            cleanUp()
            return

        # Any other input saves the current fuzz backlog
        else:
            dumpLast()

if __name__ == "__main__":
    # Parse program options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:s:a", ("port=", "seed=", "autoreload"))
    except getopt.GetoptError as err:
        print("Error:", err)
        usage()
        sys.exit(1)

    # Run the program
    print(_vBanner)
    main(opts, args)