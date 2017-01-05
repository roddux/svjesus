# Readme
SVJesus, an SVG fuzzer. With a web handler. You know the drill.

# Thoughts / musings
Most of these are probably useful ideas for RuCSS too.
RuCSS could plug-in to fuzz the style attribute.

## Implement random utility functions
### Weighted random:
LST = [("a",2), ("b",3), ("d",5)]
def weightChoice(LST):
	weightSum = sum(C[1] for C in LST)
	r = uniform(1, weightSum)
	for (choice, weight) in LST:
		r -= weight
		if r <= 0: return choice

### Random yes/no:
def coinflip(): return round(random.random()) == 0

### Classes?
- Animation elements
- Basic shapes
- Container elements
- Descriptive elements
- Filter primitive elements
- Font elements
- Gradient elements
- Graphics elements
- Graphics referencing elements
- HTML elements
- Light source elements
- Never-rendered elements
- Paint server elements
- Renderable elements
- Shape elements
- Structural elements
- Text content elements
- Text content child elements
- Uncategorized elements

All classes derived from Element, which would house global attributes
Each class would contain a list of class-generic permitted child elements
Each class would contain a list of class-generic attributes
Individual elements would add attributes and additional child elements, if need be

Named tuples can be used for classes, for things that don't change

class BasicShape(SVGElement):
	childElements = [Animation, Descriptive]

class Circle(BasicShape):
	params = {
		"x": intGen,
		"y": intGen
	}

### Generation
When generating SVGs, there would be a probability function whether to generate 
correct (as specified) data, or whether to call an alternative junk generator.

def genStuff()
	X = pick_element() # Circle()
	if should_generate_child_tags():
		genStuff()
	weighted_choice((genInvalid, 0.1), (X.genValid, 0.9))