#!/usr/bin/env python3

# Recreate the fuzz that caused a crash, as it was seen by the browser. 

# Global imports
import pickle, sys, random, time, os

# Same byte-length as the original page (noReload.html) Could be important!
_template = """
<!doctype html>
<html>
	<head>
		<title>SVJesus christ</title>
	</head>
	<body>
		<div id="target">{}</div>
		<script>
//................................................................
//................................................................
//................................................................
//...............................................................
//...............................................................
//...............................................................
//...............................................................
//...............................................................
//...............................................................
//...............................................................
//...............................................................
//...............................................................
		</script>
	</body>
</html>"""

# Option 2, in case the break relied on the loading sequence
# NOTE: The template is split in two, because {} is used as the format string.
_template2 = """
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
		fileNames = (
			"".join(
				chr(random.randint(65,90)) for _ in range(5)
			) + ".html"
			for _ in fuzzData
		)
		fileNames = list(fileNames)
		fileNames.sort()

		# Generate full-page fuzz recreations
		os.mkdir("FULL")
		os.chdir("FULL")
		for X in range(len(fuzzData)):
			with open(fileNames[X], "wb") as fullFuzzF:
				fullFuzzF.write(
					_template.format(
						fuzzData[X].decode("UTF-8")
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
				targetList.append("/"+inclName)
		with open("index.html", "w") as inclMain:
			inclMain.write(_template2.format(targetList)+_template2a)