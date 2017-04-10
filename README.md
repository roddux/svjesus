# Readme
SVJesus, an SVG fuzzer. With a web handler. You know the drill.

## Thoughts / musings
Most of these are probably useful ideas for RuCSS too.
RuCSS could plug-in to fuzz the style attribute.
Use-after-free are the most common vuln type.
Expand the codebase until it can generate known past vulnerabilities.
Modify codebase (or create a fork/patchset) that allows running on Google's ClusterFuzz.

## Implement random utility functions
- Weighted random

## Class list
- Animation elements
- Basic shapes
- Container elements
- Descriptive elements
- Filter primitive elements
- Font elements
- Gradient elements
- Graphics elements
- Graphics referencing elements
- HTML elements
- Light source elements
- Never-rendered elements
- Paint server elements
- Renderable elements
- Shape elements
- Structural elements
- Text content elements
- Text content child elements
- Uncategorized elements

## Generation ideas
When generating SVGs, there would be a probability function whether to generate 
correct (as specified) data, or whether to call an alternative junk generator.

def genStuff()
	X = pick_element() # Circle()
	if should_generate_child_tags():
		genStuff()
	weighted_choice((genInvalid, 0.1), (X.genValid, 0.9))

Or, just supply a switch to chose whether to generate correct data.

## Future plans
### Implement a curses UI
https://docs.python.org/3/howto/curses.html

### Implement a GUI
https://wiki.python.org/moin/GuiProgramming
https://riverbankcomputing.com/software/pyqt/intro
https://wiki.qt.io/PySideTutorials_Simple_Dialog

### Package it to run on Windows hosts
http://www.py2exe.org/
http://www.pyinstaller.org/
http://nuitka.net/pages/overview.html
http://cx-freeze.readthedocs.io/en/latest/overview.html

### Use a virtual desktop or equivalent to hide the browser windows 
https://technet.microsoft.com/en-us/sysinternals/cc817881.aspx

### CGroup equivalent for memory-limiting (look into this)
https://msdn.microsoft.com/en-us/library/ms684161(VS.85).aspx