#!/usr/bin/env python3

# SVJesus christ give it a rest with the puns already
# https://developer.mozilla.org/en-US/docs/Web/SVG

# All very WIP, enter at your own peril
import random

import elements 

ELEMENTS = elements.ELEMENTS

def genContent():
	return random.choice(
		(
			"".join(chr(random.randint(0,255)) for q in range(0,20)),
			"AAAAAAAAAAAAAAAAA",
			random.choice(("99999999999999", "-99999999999999")),
		)
	)

def genAnimation(attribs):
	animStr = """<animate attributeName="{}" from="{}" to="{}" dur=".1s" repeatCount="indefinite"/>"""
	return animStr.format(random.choice(attribs)["name"], genContent(), genContent())

def genAttr(tagRef, tagLst):
	randAttr = random.choice(tagLst)

	# 20% of the time, we add a duplicate tag
	if random.randint(1,100) > 20:
		del tagLst[tagLst.index(randAttr)]

	# if callable(randAttr["data"]):
		# Some attributes will have specific generators
		# content = randAttr["data"]()
	# else:
		# Fallback content generator
	content = genContent()
	# elif <custom regex string>
		# custom content generator ?

	return randAttr["name"]+"=\""+content+"\" "

def genTag():
	newTag  = random.choice(list(ELEMENTS))
	tagLst  = ELEMENTS[newTag]["attrs"].copy()
	tagRef  = ELEMENTS[newTag]
	attrStr = ""

	for _ in range(2):
		try:
			attrStr += "".join(genAttr(tagRef,tagLst))
		except Exception as e:
			# print(e)
			pass

	retStr = "<"+newTag+" "+attrStr+" "
	if round(random.random()) and len(tagLst) > 0:
			retStr += ">" + genAnimation(ELEMENTS[newTag]["attrs"]) + "</"+newTag+">"
	else:
		retStr += "/>"
	return retStr

def genStuff():
	retStr = """<svg width="%d" height="%d">""" % (random.randint(1,100), random.randint(1,100))
	retStr += (lambda: "".join(genTag() for _ in range(5)))()
	retStr += "</svg>"
	return retStr
