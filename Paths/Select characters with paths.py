# MenuTitle: Select characters with components
# Ricard Garcia (with special help from Rainer, Tosche and Mark) - 10.02.2019
# -------------------
# -*- coding: utf-8 -*-
__doc__="""
Select all of the characters that have paths in it.
"""

thisFont = Glyphs.font # frontmost font
thisMaster = thisFont.selectedFontMaster # active master
affectedGlyphs = [] # Empty list in which we are going to append the selection

for thisGlyph in thisFont.glyphs:
	# the layer with the master ID is the layer for that master:
	currentLayer = thisGlyph.layers[thisMaster.id] 
	# Checks if there's any path in the layer
	if currentLayer.paths:
		affectedGlyphs.append(thisGlyph)
		

if affectedGlyphs:
	# Adds the list of characters with paths to the selection
	thisFont.selection = affectedGlyphs
else:
	Message(title="No Components Found", message="Could not fond any components in the current master.", OKButton="Too bad")