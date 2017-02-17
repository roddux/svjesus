from svjesus.ffz import genContent
import svjesus.elements
import random

# The base class
class Element():
	# Simple method to generate an open tag with attributes
	def genOpen(self, attrCount=1):
		attrs = list(self.attrs)
		myStr = "<%s" % self.name

		# Use all attributes if we get a count too high, don't repeat
		attrCount = len(attrs) if len(attrs) < attrCount else attrCount

		# Sort out the required attributes first
		requiredAttrs = list(A for A in attrs if "required" in A and A["required"])

		# Fix up the list of attributes so we don't duplicate the required ones
		attrs = [A for A in attrs if A not in requiredAttrs]

		# Randomly select the rest
		random.shuffle(attrs)
		while attrCount:
			myAttr = requiredAttrs.pop(0) if requiredAttrs else attrs.pop(0)
			myData = myAttr["data"]
			myStr += " %s=" % myAttr["name"]
			myData = myData() if callable(myData) else myData
			myStr += "\"%s\" " % myData
			attrCount -= 1

		myStr += ">"
		return myStr

	# Method to generate a close tag
	def genClose(self):
		return "</%s>" % self.name

	# Generate a single tag with no children or attributes
	def genSingle(self, attrCount):
		return genOpen(attrCount=attrCount)+genClose()

# The SVG element
class SVG(Element):
	name = "svg"
	attrs = (
		{
			"name": "id",
			"data": "target",
			"required": True,
		},
		{
			"name": "version",
			"data": genContent,
		},
		{
			"name": "x",
			"data": genContent,
		},
		{
			"name": "y",
			"data": genContent,
		},
		{
			"name": "width",
			"data": genContent,
		},
		{
			"name": "height",
			"data": genContent,
		},
		{
			"name": "preserveAspectRatio",
			"data": genContent,
		},
		{
			"name": "contentScriptType",
			"data": genContent,
		},
		{
			"name": "contentStyleType",
			"data": genContent,
		},
		{
			"name": "viewBox",
			"data": genContent,
		},
	)

	def __init__(self):
		self.allowedChildren = (
			  svjesus.elements.Animation.__subclasses__()
			+ svjesus.elements.BasicShape.__subclasses__()
			+ svjesus.elements.Descriptive.__subclasses__()
			+ svjesus.elements.Graphic.__subclasses__()
		)