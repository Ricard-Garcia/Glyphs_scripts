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
    #print("Scale factor = %s" % (scaleFactor))
    
    myCapHeight = f.glyphs['H'].layers[0].bounds.size.width
    #print(myCapHeight)
    
    fill(0)
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
            
            #text(glyphName, (originX+boxWidth//2, originY+boxHeight*.09))
            #print(glyphName)

            
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
        fill(None)
            #fill(1, .2, .2, .2)
        strokeWidth(30*scaleFactor)
        stroke(.2)
        rect(originX + boxWidth*.25 , originY, boxWidth*.6, boxHeight*.8)
        line(
            (originX + boxWidth*.25, originY),
            (originX + boxWidth*.85, originY + boxHeight*.8)
            )
            
        line(
            (originX + boxWidth*.25, originY + boxHeight*.8),
            (originX + boxWidth*.85, originY)
            )

        #text(glyphName, (originX+boxWidth//2, originY+boxHeight*.09))


# -----------------------------
# Page settings
newPage('A4')

fill(1)
rect(0,0,width(), height())

margin = width()*.1
columns = 28
boxWidth = (width()-margin*2) / columns
#print(boxWidth)

size = 20
leading = size*1.2

# -----------------------------
# Drawing the characters

#stroke(1,0,0)
#strokeWidth(1)
line(
    (0,margin),
    (width(), margin)
    )

#originY = height()-margin
originX = margin 
#originY = height() - margin
originY = height() - margin -size       
loop = 0

for g in f.selection:
    for m in f.masters:
    #for m in f.masters[:1]:

        pathToDraw = g.layers[m.id]
        #print(pathToDraw.parent.name)

        if loop == 0:

            #Function
            glyph2draw(pathToDraw, (originX, originY), boxWidth, size) 
         
        else:

            if originX > width()-margin*2 and originY < margin*1.5:
                 #print("New page needed")                 
                 loop = 0
                 
                 originX = margin
                 originY = height() - margin - size 


                 # Page settings
                 newPage('A4')
                 fill(1)
                 rect(0,0,width(), height())
                 
                 #stroke(1,0,0)
                 #strokeWidth(1)
                 line(
                     (0,margin),
                     (width(), margin)
                  )

                 #Function
                 glyph2draw(pathToDraw, (originX, originY), boxWidth, size)
                 
            elif originX > width()-margin*2:
                #print('originX out of the page')
                #print("Origin x out of the width:", originX)
                #with savedState():
                    
                originX = margin
                originY = originY-leading
                translate(0, 0)
                
                # Circle guide
                #fill(1,0,0)
                #oval(
                #    originX-2,
                #    originY-2, 
                #    4,
                #    4)
                    
                #Function
                glyph2draw(pathToDraw, (originX, originY), boxWidth, size) 
                
                #loop = 0

            else: 
                originX = originX + boxWidth

                #Function
                glyph2draw(pathToDraw, (originX, originY), boxWidth, size)

                fill(0,0,1)
                #oval(
                #    originX-2,
                #    originY-2, 
                #    4,
                #    4)
 
        loop += 1

# Save .pdf
saveImage("~/Desktop/%s-CharacterSet.pdf"%(f.familyName))
