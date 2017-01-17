#!/usr/bin/env python3

# Recreate the fuzz that caused a crash, as it was seen by the browser. 

# Global imports
import pickle, sys, random, time, os

# Same byte-length as the original page (noReload.html) Could be important!
# TODO: This is no longer the same byte-length, fix pls
_template = """\
<!doctype html>
<html>
	<head>
		<title>SVJesus christ</title>
		<meta charset="UTF-8">
		<meta http-equiv="refresh" content="1;URL='http://localhost:8000{URL}'">
	</head>
	<body onload="jsMess()">
		<div id="target">{TRG}</div>
		<script>{SCRIPT}</script>
	</body>
</html>"""

_fuzzScript = """\
function jsMess() {
	var target = document.getElementById("target").childNodes[0];
	target.append("ASDF");
	target.removeChild(target.childNodes[1]);
	target.childNodes[0].innerHTML = "bluh";
}"""

# Option 2, in case the break relied on the loading sequence
# NOTE: The template is split in two, because {} is used as the format string.
_template2 = """\
<!doctype html>
<html>
	<head>
		<title>SVJesus christ</title>
	</head>
	<body>
		<div id="target"></div>
		<script>
			var targetList = {};"""
_template2a = """
			var target   = document.getElementById("target");
			var _loaded = false;
			var _curFuz = 0;
			function doFuzz() {
				if (_curFuz == targetList.length) { return; }
				var xhr = new XMLHttpRequest();
				xhr.open("GET", targetList[_curFuz], true);
				xhr.onload = function () {
					if (xhr.readyState == xhr.DONE) {
							target.innerHTML = xhr.responseText;
					}
					_loaded = true;
				};
				xhr.send(null);
				function loadWait() {
					if (! _loaded) setTimeout(loadWait, 0);
					else {
						_curFuz++; doFuzz();
					}
				}
				loadWait();
			}
			doFuzz();
		</script>
	</body>
</html>"""

# Script to start the http server
_serveScript = """\
#!/usr/bin/env bash
python -m http.server
"""

if __name__ == "__main__":
	# Load the pickled fuzz data
	if len(sys.argv) < 2:
		fuzzyPickleName = input("Fuzzy pickle filename: ")
	else:
		fuzzyPickleName = sys.argv[1]
	with open(fuzzyPickleName, "rb") as fuzzyPickleFile:
		try:
			fuzzData = pickle.load(fuzzyPickleFile)
		except pickle.UnpicklingError as e:
			print("Error unpickling data:", e)
			sys.exit(1)

		# Setup output directory
		outputDirName = time.strftime("OUTPUT_%Y%m%d_%H-%M-%S")
		try:
			os.mkdir(outputDirName)
			os.chdir(outputDirName)
		except Exception as e:
			print("Error setting up output directory:",e)
			sys.exit(1)

		# Ensure output files are in the same order as the fuzz data
		fileNames = [
			"".join(
				chr(random.randint(65,90)) for _ in range(5)
			) + ".html"
			for _ in fuzzData
		]
		fileNames.sort()

		# Generate full-page fuzz recreations
		os.mkdir("FULL")
		os.chdir("FULL")
		for X in range(len(fuzzData)):
			with open(fileNames[X], "wb") as fullFuzzF:
				nextFile = ""
				try:
					nextFile = fileNames[X+1]
				except:
					pass
				fullFuzzF.write(
					_template.format(
						**{
						"URL":"/FULL/"+nextFile,
						"TRG":fuzzData[X].decode("UTF-8"),
						"SCRIPT":_fuzzScript
						}
					).encode("UTF-8")
				)

		# Generate a page to load in the fuzz samples, in the same order
		os.chdir("..")
		os.mkdir("INCLUDE")
		os.chdir("INCLUDE")
		targetList = []
		for X in range(len(fuzzData)):
			inclName = "incl_"+fileNames[X]
			with open(inclName, "wb") as inclFuzzF:
				inclFuzzF.write(fuzzData[X])
				targetList.append("/INCLUDE/"+inclName)
		with open("index.html", "w") as inclMain:
			inclMain.write(_template2.format(targetList)+_template2a)

		# Write the serve script
		os.chdir("..")
		with open("serve.sh", "w") as serveScriptFile:
			serveScriptFile.write(_serveScript)
			os.chmod("serve.sh", 0o700)