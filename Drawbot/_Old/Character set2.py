from GlyphsApp import *
from drawBot import *

# Variables
f = Glyphs.font
myLayers = Glyphs.font.selectedLayers


# Function that draws the glyphs
def glyph2draw(layer, boxOrigin, boxWidth, boxHeight = 20, font = f):
    
    #fill(0.9)
    stroke(0)
    strokeWidth(0)
    
    originX, originY = boxOrigin
    
    scaleFactor = boxHeight/(f.masters[0].capHeight*2)
    
    myCapHeight = f.glyphs['H'].layers[0].bounds.size.width
    print(myCapHeight)
    
    fill(0.9)
    stroke(0)
    strokeWidth(0)

    if layer.bounds.size.width > 0:
        with savedState():
            fill(.9, .2)
            #fill(1, .2, .2, .2)
            strokeWidth(1)
            stroke(1)
            rect(originX, originY, boxWidth, boxHeight)
            
            
        with savedState():
            scale(scaleFactor, scaleFactor, center = (originX, originY))
            translate(originX+90, originY+(myCapHeight/2)) # * = unpacking tuple
            print(originX)
            translate(
                ((boxWidth - layer.bounds.size.width * scaleFactor) / 2)/scaleFactor
                )
            # Drawing the glpyh
            drawPath(layer.completeBezierPath)
    

# -----------------------------
# Page settings
newPage('A4')

fill(.05)
rect(0,0,width(), height())

margin = width()*.1
columns = 18
boxWidth = (width()-margin*.2) / columns

# -----------------------------
# Drawing the characters

#originY = height()-margin
originX = margin

loop = 0

for g in f.selection:
    for m in f.masters:
        pathToDraw = g.layers[m.id]
        originX = 30 + loop*boxWidth   
        #originX = margin + columns * boxWidth
        originY = height() - margin
        print(originX, originY)
        glyph2draw(pathToDraw, (originX, originY), boxWidth) 
 
        loop += 1
# if layer[0] do draw. 
# else: pass