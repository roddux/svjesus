#!/usr/bin/env python3

# SVJesus christ give it a rest with the puns already
# https://developer.mozilla.org/en-US/docs/Web/SVG

# Content generation and utility functions will be moved
import random
def coinflip(): return random.choice((True,False))
def genContent():
	return random.choice(
		(
			# "".join(chr(random.randint(0,255)) for q in range(0,20)),
			"AAAAAAAAAAAAAAAAA",
			random.choice(("99999999999999", "-99999999999999")),
		)
	)

import svjesus.elements

# Generate a bunch of elements
# TODO: Need a way to pass valid arguments to this function, for use as attributes
def genTags(recurseCount=10, pickList=None):
	totalTags = 10
	retStr = ""

	# Continue generating tags until we hit the limit
	while totalTags > 0:
		# If we're not limited to certain tags, chose from the whole list
		if pickList == None:
			tag = random.choice(svjesus.elements.elementList)()
		# Otherwise chose from the list supplied
		else:
			if len(pickList) == 0: break
			tag = random.choice(pickList)()

		# Increase generated tag count
		totalTags = totalTags - 1

		# A high attrCount uses all of the attributes, doesn't duplicate
		retStr += tag.genOpen(attrCount=3)

		# Maybe recurse, if we're under the limit
		if recurseCount and coinflip() and coinflip() and coinflip():
			recurseCount = recurseCount-1
			# mStr,totalTags=genTags(recurseCount=recurseCount, pickList=(tag.allowedChildren))
			mStr,totalTags=genTags(recurseCount=recurseCount, pickList=(svjesus.elements.elementList))
			retStr += mStr

		# Add the closer
		retStr += tag.genClose()+"\n"

	return retStr,totalTags

# The main function
def genSVG():
	SVG = svjesus.elements.Base.SVG()
	retStr  = SVG.genOpen(attrCount=5)
	retStr += genTags(pickList=SVG.allowedChildren)[0]
	retStr += SVG.genClose()
	return retStr