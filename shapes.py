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
				}
			]
			# ].extend(globalAttrs)
			# Extend now, or when generating fuzz data at runtime?
			# Which is faster/lower footprint? Speed is more important.
			# => Profiling
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
				}
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
				}
			]
	},
	"polygon": {
		"attrs":
			[
				{
					"name": "points",
					# "data": genContent
				}
			]
	},
	"polyline": {
		"attrs":
			[
				{
					"name": "points",
					# "data": genContent
				}
			]
	}
}

globalAttrs = (
	#requiredExtensions, requiredFeatures, systemLanguage,
	#id, xml:base, xml:lang, xml:space, tabindex,
	#onabort, onerror, onresize, onscroll, onunload, onzoom,
	#height, result, width, x, y,
	#onactivate, onclick, onfocusin, onfocusout, onload, onmousedown, onmousemove, onmouseout, onmouseover, onmouseup,
	#type, tableValues, slope, intercept, amplitude, exponent, offset
	#xlink:href, xlink:type, xlink:role, xlink:arcrole, xlink:title, xlink:show, xlink:actuate
	{
		"name": "style",
		# "data": genContent
	}
)
