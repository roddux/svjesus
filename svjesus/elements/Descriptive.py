from svjesus.ffz import genContent
from svjesus.elements.Base import Element

class Descriptive(Element):
	def __init__(self):
		self.allowedChildren = () # TODO: Check what's allowed

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