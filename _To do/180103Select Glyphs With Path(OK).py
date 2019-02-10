#MenuTitle: Select Glyphs With Paht/Components
# -*- coding: utf-8 -*-
__doc__="""
In Font view, select glyphs with paths or components"""

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
		if displayedGlyphsInFontView[i].layers[0].paths or displayedGlyphsInFontView[i].layers[0].components:
			fontView.addSelectionIndexes_( indexSetWithIndex(i) )



# Hem eliminat la llista "colorIndexes" i treta la part de codi de selecció del glyph.