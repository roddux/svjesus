from svjesus.ffz import genContent
from svjesus.elements.Base import Element
import svjesus.elements.Descriptive

class BasicShape(Element):
	def __init__(self):
		self.allowedChildren = (
			  svjesus.elements.Descriptive.__subclasses__()
			+ svjesus.elements.Animation.__subclasses__()
		)

# BasicShape elements
class Circle(BasicShape):
	name  = "circle"
	attrs = (
		{
			"name": "cx",
			"data": genContent,
		},
		{
			"name": "cy",
			# "data": "[0-9]*"
			"data": genContent,
		},
		{
			"name": "r",
			"data": genContent,
			"required": True,
		},
	)

class Rect(BasicShape):
	name  = "rect"
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
			"name": "rx",
			"data": genContent,
		},
		{
			"name": "ry",
			"data": genContent,
		},
	)

class Ellipse(BasicShape):
	name = "ellipse"
	attrs = (
		{
			"name": "cx",
			"data": genContent,
			"required": True,
		},
		{
			"name": "cy",
			"data": genContent,
			"required": True,
		},
		{
			"name": "rx",
			"data": genContent,
			"required": True,
		},
		{
			"name": "ry",
			"data": genContent,
			"required": True,
		},
	)

class Line(BasicShape):
	name = "line"
	attrs = (
		{
			"name": "x1",
			"data": genContent,
			"required": True,
		},
		{
			"name": "x2",
			"data": genContent,
			"required": True,
		},
		{
			"name": "y1",
			"data": genContent,
			"required": True,
		},
		{
			"name": "y2",
			"data": genContent,
			"required": True,
		},
	)

class Polygon(BasicShape):
	name = "polygon"
	attrs = (
		{
			"name": "points",
			"data": genContent,
			"required": True,
		},
	)

class PolyLine(BasicShape):
	name = "polyline"
	attrs = (
		{
			"name": "points",
			"data": genContent,
			"required": True,
		},
	)