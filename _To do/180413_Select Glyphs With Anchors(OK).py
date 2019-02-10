#MenuTitle: Select Glyphs With Anchors
# -*- coding: utf-8 -*-
__doc__="""
In Font view, select glyphs with anchors"""

import GlyphsApp

def indexSetWithIndex( index ):
	indexSet = NSIndexSet.alloc().initWithIndex_( index )
	return indexSet

thisDoc = Glyphs.currentDocument # frontmost document
fontView = thisDoc.windowController().tabBarControl().viewControllers()[0].glyphsArrayController()
displayedGlyphsInFontView = fontView.arrangedObjects() # all glyphs currently displayed

if displayedGlyphsInFontView:
	displayedIndexRange = range(len(displayedGlyphsInFontView)) # indexes of glyphs in Font view
	for i in displayedIndexRange:
		if displayedGlyphsInFontView[i].layers[0].anchors or displayedGlyphsInFontView[i].layers[0].anchors:
			fontView.addSelectionIndexes_( indexSetWithIndex(i) )



# Hem eliminat la llista "colorIndexes" i treta la part de codi de selecció del glyph.
