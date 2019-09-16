from GlyphsApp import *
from drawBot import *

# Variables
f = Glyphs.font
myLayers = Glyphs.font.selectedLayers


# Function that draws the glyphs
def glyph2draw(layer, boxOrigin, boxHeight = 20, font = f):
    
    #fill(0.9)
    stroke(0)
    strokeWidth(0)
    
    originX, originY = boxOrigin
    
    
    scaleFactor = boxHeight/(f.masters[0].capHeight*2)

    boxWidthNotScale = (layer.width)
    print(boxWidthNotScale)
    
    boxWidth = (layer.width)*scaleFactor
    #print(boxWidth)

    #print(originX)
    #print(originX+boxWidth)

    #print("Scale factor = %s" % (scaleFactor))
    
    myCapHeight = f.glyphs['H'].layers[0].width
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
            #rect(originX, originY, boxWidth, boxHeight)
            
            fill(1,0,0)
            #oval(originX-5, originY-5, 10, 10)
            fill(0,0,1)  
            #oval(originX+boxWidth-5, originY-5, 10, 10)
            #text(glyphName, (originX+boxWidth//2, originY+boxHeight*.09))
            #print(glyphName)

            
        with savedState():
            scale(scaleFactor, scaleFactor, center = (originX, originY))
            translate(originX, originY) # * = unpacking tuple
            #print(originX)
            
            # Drawing the glpyh
            drawPath(layer.completeBezierPath)
        

        #with savedState():
            #translate(boxWidth, originY) # * = unpacking tuple

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
#boxWidth = (width()-margin*2) / columns
#print(boxWidth)

size = 20
leading = size*1.2

# -----------------------------
# Drawing the characters

#originY = height()-margin
originX = margin 
scaleFactor = size/(f.masters[0].capHeight*2)

#originY = height() - margin
originY = height() - margin - size        
loop = 0

for g in f.selection:

    for m in f.masters:
        boxWidth = (g.layers[m.id].width)*scaleFactor

        pathToDraw = g.layers[m.id]
        print(pathToDraw.parent.name)
        #boxWidth = (g.layers[m.id].bounds.size.width)*scaleFactor


        if loop == 0:

            #Function

            glyph2draw(pathToDraw, (originX, originY), size) 
        

    
        else:
            
            if originX > width()-margin*2:
                #print('originX out of the page')
                #print("Origin x out of the width:", originX)
                with savedState():
                    
                    originX = margin
                    originY = originY-leading
                    translate(0, 0)

                    
                #Function
                    glyph2draw(pathToDraw, (originX, originY), size) 

                loop = 0

            elif originY < margin:
                 print("New page needed")

                 originX = margin 
                 originY = height() - margin - size 

                 # Page settings
                 newPage('A4')
                 fill(.05)
                 rect(0,0,width(), height())

                 #Function
                 glyph2draw(pathToDraw, (originX, originY), size)   
                
            else: 

                

                #Function
                glyph2draw(pathToDraw, (originX, originY), size)
                
        originX = originX + boxWidth+2

               
        loop += 1
        

saveImage("~/Desktop/firstImage.pdf")


    