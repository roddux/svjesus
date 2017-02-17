from svjesus.ffz import genContent
from svjesus.elements.Base import Element

# http://stackoverflow.com/questions/72852/how-to-do-relative-imports-in-python
# http://stackoverflow.com/questions/9277200/multilevel-relative-import

class Animation(Element):
	def __init__(self):
		self.allowedChildren = () # TODO: Check what's allowed


# Animation elements
class Animate(Animation):
	name = "animate"
	attrs = (
		{
			"name": "attributeName",
			"data": genContent,
			"required": True,
		},
		{
			"name": "attributeType",
			"data": genContent,
		},
		{
			"name": "from",
			"data": genContent,
			"required": True,
		},
		{
			"name": "to",
			"data": genContent,
			"required": True,
		},
		{
			"name": "dur",
			"data": genContent,
			"required": True,
		},
		{
			"name": "repeatCount",
			"data": genContent,
			"required": True,
		},
		{
			"name": "begin",
			"data": genContent,
		},
		{
			"name": "end",
			"data": genContent,
		},
		{
			"name": "min",
			"data": genContent,
		},
		{
			"name": "max",
			"data": genContent,
		},
		{
			"name": "restart",
			"data": genContent,
		},
		{
			"name": "repeatDur",
			"data": genContent,
		},
		{
			"name": "fill",
			"data": genContent,
		},
		{
			"name": "additive",
			"data": genContent,
		},
		{
			"name": "accumulate",
			"data": genContent,
		},
		{
			"name": "calcMode",
			"data": genContent,
		},
		{
			"name": "values",
			"data": genContent,
		},
		{
			"name": "keyTimes",
			"data": genContent,
		},
		{
			"name": "keySplines",
			"data": genContent,
		},
		{
			"name": "by",
			"data": genContent,
		},
		{
			"name": "autoReverse",
			"data": genContent,
		},
		{
			"name": "accelerate",
			"data": genContent,
		},
		{
			"name": "decelerate",
			"data": genContent,
		},
	)