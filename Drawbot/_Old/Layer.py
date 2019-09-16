from GlyphsApp import *

myLayers = Glyphs.font.selectedLayers

for thisLayer in myLayers:
    print thisLayer.parent.name
    #print thisLayer.paths