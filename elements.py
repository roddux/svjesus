#!/usr/bin/env python3
import random, ffz

# Still need to add content generators, for tags that actually contain content
# rather than just more tags-- such as the 'title', 'desc' and 'text' tags.

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
			"data": ffz.genContent,
		},
		{
			"name": "x",
			"data": ffz.genContent,
		},
		{
			"name": "y",
			"data": ffz.genContent,
		},
		{
			"name": "width",
			"data": ffz.genContent,
		},
		{
			"name": "height",
			"data": ffz.genContent,
		},
		{
			"name": "preserveAspectRatio",
			"data": ffz.genContent,
		},
		{
			"name": "contentScriptType",
			"data": ffz.genContent,
		},
		{
			"name": "contentStyleType",
			"data": ffz.genContent,
		},
		{
			"name": "viewBox",
			"data": ffz.genContent,
		},
	)

	def __init__(self):
		self.allowedChildren = (
			Descriptive.__subclasses__()
			+ Animation.__subclasses__()
			+ Graphic.__subclasses__()
			+ BasicShape.__subclasses__()
		)

# Element groups
class Descriptive(Element):
	def __init__(self):
		self.allowedChildren = () # TODO: Check what's allowed

class Animation(Element):
	def __init__(self):
		self.allowedChildren = () # TODO: Check what's allowed

class Graphic(Element):
	def __init__(self):
		self.allowedChildren = () # TODO: Check what's allowed

class BasicShape(Element):
	def __init__(self):
		self.allowedChildren = (
			Descriptive.__subclasses__()+Animation.__subclasses__()
		)


# BasicShape elements
class Circle(BasicShape):
	name  = "circle"
	attrs = (
		{
			"name": "cx",
			"data": ffz.genContent,
		},
		{
			"name": "cy",
			# "data": "[0-9]*"
			"data": ffz.genContent,
		},
		{
			"name": "r",
			"data": ffz.genContent,
			"required": True,
		},
	)

class Rect(BasicShape):
	name  = "rect"
	attrs = (
		{
			"name": "x",
			"data": ffz.genContent,
		},
		{
			"name": "y",
			"data": ffz.genContent,
		},
		{
			"name": "width",
			"data": ffz.genContent,
			"required": True,
		},
		{
			"name": "height",
			"data": ffz.genContent,
			"required": True,
		},
		{
			"name": "rx",
			"data": ffz.genContent,
		},
		{
			"name": "ry",
			"data": ffz.genContent,
		},
	)

class Ellipse(BasicShape):
	name = "ellipse"
	attrs = (
		{
			"name": "cx",
			"data": ffz.genContent,
			"required": True,
		},
		{
			"name": "cy",
			"data": ffz.genContent,
			"required": True,
		},
		{
			"name": "rx",
			"data": ffz.genContent,
			"required": True,
		},
		{
			"name": "ry",
			"data": ffz.genContent,
			"required": True,
		},
	)

class Line(BasicShape):
	name = "line"
	attrs = (
		{
			"name": "x1",
			"data": ffz.genContent,
			"required": True,
		},
		{
			"name": "x2",
			"data": ffz.genContent,
			"required": True,
		},
		{
			"name": "y1",
			"data": ffz.genContent,
			"required": True,
		},
		{
			"name": "y2",
			"data": ffz.genContent,
			"required": True,
		},
	)

class Polygon(BasicShape):
	name = "polygon"
	attrs = (
		{
			"name": "points",
			"data": ffz.genContent,
			"required": True,
		},
	)

class PolyLine(BasicShape):
	name = "polyline"
	attrs = (
		{
			"name": "points",
			"data": ffz.genContent,
			"required": True,
		},
	)


# Descriptive elements
class Desc(Descriptive):
	name = "desc"
	attrs = ()

class Metadata(Descriptive):
	name = "metadata"
	attrs = ()

class Title(Descriptive):
	name = "title"
	attrs = ()


# Graphic elements
class Image(Graphic):
	name = "image"
	attrs = (
		{
			"name": "x",
			"data": ffz.genContent,
		},
		{
			"name": "y",
			"data": ffz.genContent,
		},
		{
			"name": "width",
			"data": ffz.genContent,
			"required": True,
		},
		{
			"name": "height",
			"data": ffz.genContent,
			"required": True,
		},
		{
			"name": "xlink:href",
			"data": ffz.genContent,
			"required": True,
		},
		{
			"name": "preserveAspectRatio",
			"data": ffz.genContent
		},
	)

class Text(Graphic):
	name = "text"
	attrs = (
		{
			"name": "x",
			"data": ffz.genContent
		},
		{
			"name": "y",
			"data": ffz.genContent
		},
		{
			"name": "dx",
			"data": ffz.genContent
		},
		{
			"name": "dy",
			"data": ffz.genContent
		},
		{
			"name": "text-anchor",
			"data": ffz.genContent
		},
		{
			"name": "rotate",
			"data": ffz.genContent
		},
		{
			"name": "textLength",
			"data": ffz.genContent
		},
		{
			"name": "lengthAdjust",
			"data": ffz.genContent
		},
	)

# TODO: Fancy subclassing magic to grab all emenents
ELEMENTS = (Circle,Rect,Ellipse,Line,Polygon,PolyLine,Desc,Metadata,Title,Image,Text)

# Debug mode to check progress
if __name__ == "__main__":
	count = len(ELEMENTS)
	print("Total elements: %d out of %d (%.2f%%)" % (count, 94, count/94 * 100))