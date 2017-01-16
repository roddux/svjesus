# here be dragons
basicShapes = {
	"circle": {
		"attrs":
			[
				{
					"name": "cx",
					# "data": genContent
					# "data": <function reference> ?
					# if callable(tags[tag][attr][N][data]): [..]
				},
				{
					"name": "cy",
					# "data": "[0-9]*"
					# "data": genContent
				},
				{
					"name": "r",
					# "data": genContent
				},
			]
	},
	"ellipse": {
		"attrs":
			[
				{
					"name": "cx",
					# "data": genContent
				},
				{
					"name": "cy",
					# "data": genContent
				},
				{
					"name": "rx",
					# "data": genContent
				},
				{
					"name": "ry",
					# "data": genContent
				},
			]
	},
	"line": {
		"attrs":
			[
				{
					"name": "x1",
					# "data": genContent
				},
				{
					"name": "x2",
					# "data": genContent
				},
				{
					"name": "y1",
					# "data": genContent
				},
				{
					"name": "y2",
					# "data": genContent
				},
			]
	},
	"polygon": {
		"attrs":
			[
				{
					"name": "points",
					# "data": genContent
				},
			]
	},
	"polyline": {
		"attrs":
			[
				{
					"name": "points",
					# "data": genContent
				},
			]
	},
	"rect": {
		"attrs":
			[
				{
					"name": "x",
					# "data": genContent
				},
				{
					"name": "y",
					# "data": genContent
				},
				{
					"name": "width",
					# "data": genContent
				},
				{
					"name": "height",
					# "data": genContent
				},
				{
					"name": "rx",
					# "data": genContent
				},
				{
					"name": "ry",
					# "data": genContent
				},
			]
	},
}

descriptive = {
	"desc": {
		"attrs": []
	},
	"metadata": {
		"attrs": []
	},
	"title": {
		"attrs": []
	},
}

graphicElements = {
	"image": {
		"attrs":
			[
				{
					"name": "x",
				},
				{
					"name": "y",
				},
				{
					"name": "width",
				},
				{
					"name": "height",
				},
				{
					"name": "xlink:href",
				},
				{
					"name": "preserveAspectRatio",
				},
			]
	},
	# "mesh": {
	# 	"attrs":
	# 		[
	# 			{
	# 				"name": "",
	# 			},
	# 		]
	# },
	"text": {
		"attrs":
			[
				{
					"name": "x",
				},
				{
					"name": "y",
				},
				{
					"name": "dx",
				},
				{
					"name": "dy",
				},
				{
					"name": "text-anchor",
				},
				{
					"name": "rotate",
				},
				{
					"name": "textLength",
				},
				{
					"name": "lengthAdjust",
				},
			]
	},
	# "use": {
	# 	"attrs":
	# 		[
	# 			{
	# 				"name": "",
	# 			},
	# 		]
	# },
}

ELEMENTS = basicShapes
ELEMENTS.update(descriptive)
ELEMENTS.update(graphicElements)

# To check progress!
if __name__ == "__main__":
	count = len(descriptive)+len(basicShapes)+len(graphicElements)
	print("Total elements: %d out of %d (%.2f%%)" % (count, 94, count/94 * 100))