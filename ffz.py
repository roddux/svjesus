#!/usr/bin/env python3

# SVJesus christ give it a rest with the puns already
# https://developer.mozilla.org/en-US/docs/Web/SVG

# All very WIP, enter at your own peril
import random

def genContent():
	return random.choice(
		(
			"".join(chr(random.randint(0,255)) for q in range(0,20)),
			"AAAAAAAAAAAAAAAAA",
			random.choice(("99999999999999", "-99999999999999")),
		)
	)

def genAnimation():
	return random.choice(
		(
			"""<animate attributeName="x" from="-1000" to="1000" dur=".1s" repeatCount="indefinite"/>""",
			"""<animate attributeName="y" from="-1000" to="1000" dur=".1s" repeatCount="indefinite"/>""",
		)
	)

def genAttr(tagRef, tagLst):
	randAttr = random.choice(tagLst)

	# 20% of the time, we add a duplicate tag
	if random.randint(1,100) > 20:
		del tagLst[tagLst.index(randAttr)]

	if callable(randAttr["data"]):
		# Some attributes will have specific generators
		content = randAttr["data"]()
	else:
		# Fallback content generator
		content = genContent()

	return randAttr["name"]+"=\""+content+"\" "

def genTag():
	newTag  = random.choice(list(basicShapes))
	tagLst  = basicShapes[newTag]["attrs"].copy()
	tagRef  = basicShapes[newTag]
	attrStr = ""

	for _ in range(2):
		try:
			attrStr += "".join(genAttr(tagRef,tagLst))
		except Exception as e:
			# print(e)
			pass

	retStr = "<"+newTag+" "+attrStr+" "
	if round(random.random()):
		retStr += ">" + genAnimation() + "</"+newTag+">"
	else:
		retStr += "/>"
	return retStr

def genStuff():
	retStr = """<svg width="%d" height="%d">""" % (random.randint(1,100), random.randint(1,100))
	retStr += (lambda: "".join(genTag() for _ in range(5)))()
	retStr += "</svg>"
	return retStr

# here be dragons
basicShapes = {
	"circle": {
		"attrs":
			[
				{
					"name": "cx",
					"data": genContent
					# "data": <function reference> ?
					# if callable(tags[tag][attr][N][data]): [..]
				},
				{
					"name": "cy",
					# "data": "[0-9]*"
					"data": genContent
				},
				{
					"name": "r",
					"data": genContent
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
					"data": genContent
				},
				{
					"name": "y",
					"data": genContent
				},
				{
					"name": "width",
					"data": genContent
				},
				{
					"name": "height",
					"data": genContent
				},
				{
					"name": "rx",
					"data": genContent
				},
				{
					"name": "ry",
					"data": genContent
				}
			]
	},
	"ellipse": {
		"attrs":
			[
				{
					"name": "cx",
					"data": genContent
				},
				{
					"name": "cy",
					"data": genContent
				},
				{
					"name": "rx",
					"data": genContent
				},
				{
					"name": "ry",
					"data": genContent
				}
			]
	},
	"polygon": {
		"attrs":
			[
				{
					"name": "points",
					"data": genContent
				}
			]
	},
	"polyline": {
		"attrs":
			[
				{
					"name": "points",
					"data": genContent
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
		"data": genContent
	}
)
