#MenuTitle: Select Metric Errors
# -*- coding: utf-8 -*-
__doc__="""
In Font view, select glyphs with metric errors.
"""

import GlyphsApp

def indexSetWithIndex( index ):
	indexSet = NSIndexSet.alloc().initWithIndex_( index )
	return indexSet

thisFont = Glyphs.font
thisDoc = Glyphs.currentDocument # frontmost document
fontView = thisDoc.windowController().tabBarControl().viewControllers()[0].glyphsArrayController()
displayedGlyphsInFontView = fontView.arrangedObjects() # all glyphs currently displayed
pp = []

if displayedGlyphsInFontView:
	displayedIndexRange = range(len(displayedGlyphsInFontView)) # indexes of glyphs in Font view
	for i in displayedIndexRange:
		if fontView.selectionIndexes().containsIndex_(i):
			#pp.append(dir(displayedGlyphsInFontView[i].layers[0])) #dir(dona tots els atributs d'un objecte)
			print "Left:" displayedGlyphsInFontView[i].layers[0].leftMetricsKeyIsInSync() "& Right:" displayedGlyphsInFontView[i].layers[0].rightMetricsKeyIsInSync()
#print pp


#<native-selector leftMetricsKeyIsInSync of <GSLayer "Light Extended" (P)>> dona error per què és un mètode (necessita parèntesis).