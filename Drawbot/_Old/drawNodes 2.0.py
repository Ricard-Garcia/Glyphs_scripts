from GlyphsApp import *
from drawBot import *

font = Glyphs.font
layer = font.selectedLayers[0]

fill(0.9)
strokeWidth(3)
stroke(0)		
drawPath(layer.completeBezierPath)

d = 20
r = d/2

for i, path in enumerate(layer.paths):
	#print(i, path)
	
	for i, node in enumerate(path.nodes):
	    xNode, yNode = node.position
	    if node.type == "offcurve":
	        fill(1, 0, 0)
	        oval(
	            xNode - r,
	            yNode - r,
	            d,
	            d
	            )
	        fill(None)
	    
	    elif node.type == "curve":
	        fill(0, 1, 0)
	        oval(
	            xNode - r,
	            yNode - r,
	            d,
	            d
	            )
	        fill(None)
	        
	        # Previous 3rd point
	        p3X, p3Y = path.nodes[i-3].position
	        
	        # Previous 2rd point
	        p2X, p2Y = path.nodes[i-2].position
	        
	        # Previous point
	        p1X, p1Y = path.nodes[i-1].position
	        
	        stroke(1, 0, 0)
	        line(
	            (p3X, p3Y),
	            (p2X, p2Y)
	            )
	            
	        line(
	            (p1X, p1Y),
	            (xNode, yNode)
	            )
	        
	        stroke(None)
	        
	    else:
	        fill(0, 0, 1)
	        oval(
	            xNode - r,
	            yNode - r,
	            d,
	            d
	            )
	        fill(None)
	        

