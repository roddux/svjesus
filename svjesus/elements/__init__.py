from svjesus.elements.Animation import *
from svjesus.elements.BasicShape import *
from svjesus.elements.Descriptive import *
from svjesus.elements.Graphic import *

# TODO: Fancy subclassing magic to grab all emenents
elementList = (
	# Animation
	Animate,

	# BasicShape
	Circle,
	Rect,
	Ellipse,
	Line,
	Polygon,
	PolyLine,

	# Descriptive
	Desc,
	Metadata,
	Title,

	# Graphic
	Image,
	Text
)