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
    
    fill(0.9)
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
            rect(originX, originY, boxWidth, boxHeight)
            
            text(glyphName, (originX+boxWidth//2, originY+boxHeight*.09))
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
        pass
        #with savedState():
            #fill(.9, .2)
            #fill(1, .2, .2, .2)
            #strokeWidth(1)
            #stroke(1)
            #rect(originX-boxHeight, originY, boxWidth, boxHeight)
    

# -----------------------------
# Page settings
newPage('A4')

fill(.05)
rect(0,0,width(), height())

margin = width()*.1
columns = 5
boxWidth = (width()-margin*2) / columns
print(boxWidth)

size = 50
leading = size*1.2

scaleFactor = size/(f.masters[0].capHeight*2)


# -----------------------------
# Drawing the characters

#originY = height()-margin
originX = margin 
#originY = height() - margin
originY = height() - margin - size        
loop = 0

for g in f.selection:
    for m in f.masters:
        boxWidth = (g.layers[m.id].bounds.size.width)*scaleFactor*2
        print(boxWidth)
        pathToDraw = g.layers[m.id]
        print(pathToDraw.parent.name)

        if loop == 0:

            #Function
            glyph2draw(pathToDraw, (originX, originY), boxWidth, size) 
    
        else:
            if originX > width()-margin*2:
                #print('originX out of the page')
                #print("Origin x out of the width:", originX)
                with savedState():
                    
                    originX = margin
                    originY = originY-leading
                    translate(0, 0)

                    
                #Function
                    glyph2draw(pathToDraw, (originX, originY), boxWidth, size) 

                loop = 0

            elif originY < margin:
                 print("New page needed")
                 #pass 
                 #originY = height()-margin
                 #originX = margin 
                 #originY = height() - margin
                 
                 originX = margin 
                 originY = height() - margin - size 

                 # Page settings
                 newPage('A4')
                 fill(.05)
                 rect(0,0,width(), height())

                 #Function
                 glyph2draw(pathToDraw, (originX, originY), boxWidth, size)   
                
            else: 
                originX = originX + boxWidth


                #Function
                glyph2draw(pathToDraw, (originX, originY), boxWidth, size)


        #originY = height() - margin
        #glyph2draw(pathToDraw, (originX, originY), boxWidth) 
 
        loop += 1
# if layer[0] do draw. 
# else: pass