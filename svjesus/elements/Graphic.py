from svjesus.ffz import genContent
from svjesus.elements.Base import Element

class Graphic(Element):
	def __init__(self):
		self.allowedChildren = () # TODO: Check what's allowed

# Graphic elements
class Image(Graphic):
	name = "image"
	attrs = (
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
			"required": True,
		},
		{
			"name": "height",
			"data": genContent,
			"required": True,
		},
		{
			"name": "xlink:href",
			"data": genContent,
			"required": True,
		},
		{
			"name": "preserveAspectRatio",
			"data": genContent
		},
	)

class Text(Graphic):
	name = "text"
	attrs = (
		{
			"name": "x",
			"data": genContent
		},
		{
			"name": "y",
			"data": genContent
		},
		{
			"name": "dx",
			"data": genContent
		},
		{
			"name": "dy",
			"data": genContent
		},
		{
			"name": "text-anchor",
			"data": genContent
		},
		{
			"name": "rotate",
			"data": genContent
		},
		{
			"name": "textLength",
			"data": genContent
		},
		{
			"name": "lengthAdjust",
			"data": genContent
		},
	)