from GlyphsApp import *
from drawBot import *

# Variables
f = Glyphs.font
myLayers = Glyphs.font.selectedLayers


for g in f.selection:
    for l in myLayers:
        layerToDraw = g.layers[f.selectedFontMaster.id]
        
        fill(None)
        stroke(0)
        drawPath(layerToDraw.completeBezierPath)
        
        stroke(None)
        for path in layerToDraw.paths:
            for node in path.nodes:
                diameter = 10
                
                # Dictionary of nodes
                #nodes = {}
            
                nodeX, nodeY = node.position 
                print(node.position, node.type)
            
                if node.type == "line" or node.type == "curve":
                    fill(1,0,0)
    
                elif node.type == "offcurve":
    
                    fill(0,0,1)



                oval(
                    nodeX - diameter//2,
                    nodeY - diameter//2,
                    diameter,
                    diameter
                    )
        

saveImage("~/Desktop/%s-nodes.pdf"% (g.name))