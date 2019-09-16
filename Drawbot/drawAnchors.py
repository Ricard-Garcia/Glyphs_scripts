from GlyphsApp import *
from drawBot import *

f = Glyphs.font
myLayers = Glyphs.font.selectedLayers

def glyphWithAnchors(layer, boxOrigin, boxWidth, boxHeight = 20, font = f):
    
    #fill(0.9)
    stroke(0)
    strokeWidth(0)
    
    originX, originY = boxOrigin
    
    scaleFactor = boxHeight/(f.masters[0].capHeight*2)
    #print("Scale factor = %s" % (scaleFactor))
    
    myCapHeight = f.glyphs['H'].layers[0].bounds.size.width
    #print(myCapHeight)
    
    fill(0.2,.3)
    stroke(0)
    strokeWidth(0)
    
    
    
    glyphName = FormattedString()
    glyphName.append(str(layer.parent.name), font="Helvetica", fontSize = boxHeight*.08, fill = (1,0,0))
    


    if layer.bounds.size.width > 0:
        with savedState():
            fill(0.3)
            #fill(1, .2, .2, .2)
            strokeWidth(50*scaleFactor)
            stroke(1)
            #rect(originX, originY, boxWidth, boxHeight)
            
            text(glyphName, (originX+boxWidth//2, originY+boxHeight*.09))
            #print(glyphName)
            
            # --------------------
            # DRAW ANCHORS
            # --------------------

            
        with savedState():
            scale(scaleFactor, scaleFactor, center = (originX, originY))
            translate(originX, originY+(myCapHeight/2)) # * = unpacking tuple
            #print(originX)
            translate(
                ((boxWidth - layer.bounds.size.width * scaleFactor) / 2)/scaleFactor
                )
            # Drawing the glpyh
            drawPath(layer.completeBezierPath)
    else:
        pass
        #with savedState():
            #fill(.9, .2)
            #fill(1, .2, .2, .2)
            #strokeWidth(1)
            #stroke(1)
            #rect(originX-boxHeight, originY, boxWidth, boxHeight)
    
    
    
newPage("A4")
fill(1)
rect(
   0,
   0,
   width(),
   height() 
    )
    
margin = width()*.05
originX = margin*10
originY = margin

for g in f.selection:
    for m in f.masters:
        pathToDraw = g.layers[m.id]
        print(pathToDraw.parent.name)
 
        glyphWithAnchors(pathToDraw, (originX, originY), 100, 800, f)

    