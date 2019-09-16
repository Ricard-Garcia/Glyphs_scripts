from GlyphsApp import *
from drawBot import *

# Variables
f = Glyphs.font
myLayers = Glyphs.font.selectedLayers

# UI
#Variable([
#    dict(name="Guidelines", ui="CheckBox")
#    ], globals())

# Function that draws the glyphs
def glyph2draw(layer, originX, originY, boxWidth, pointSize, leading, font = f):
    #print(pointSize, leading)
    
    # create a fresh bezier path
    #path = BezierPath()
    
    fill(.9, .2)


    #print(layer.bounds)
    a, b = layer.bounds
    #print(a, b)
    
    minx, miny = a
    maxx, maxy = b
    print(minx, miny, maxx, maxy)
    characterW = maxx - minx
    characterH = maxy - miny
    
    # Bezier path
    with savedState():
        translate(originX - characterW//2, (originY-characterH//2)+h*0.02)
        drawPath(layer.bezierPath)
    
    print("Character height is:", characterH)
    print("Character width is:", characterW)
        
    print("Bounds done!")
    #print(font)

   
# --------------------------------------------------------    
w = 1000
h = w

newPage(w, h)
fill(.05)
rect(0, 0, w, h)

margin = w*.03
 
thisMaster = f.selectedFontMaster # active master 
    
columns = 44
rows = 5
boxWidth = (width() - 2*margin)/columns
    
pointSize = 210
leading = pointSize*1.2
    
originX = w/2

loopCount = 0
originY = h/2

for g in f.selection:
    #print(g)
    #layer = g.layers[thisMaster.id]
    for thisLayer in g.layers:

        glyph2draw(thisLayer, originX, originY, boxWidth, pointSize, leading)
    

# Guidelines
if Guidelines:

    dotColumns = 10
    step = w/dotColumns   
    #print(step)

    stroke(1,0,0)
    line((width()//2, 0), (width()//2, h) )

    # Margins
    line((margin, 0), (margin, h) )
    line((w-margin, 0), (w-margin, h) )
    line((0, h-margin), (w, h-margin) )
    line((0, margin), (w, margin) )

    for d in range(dotColumns+1):
        fill(1,0,0)
        strokeWidth(1)
        stroke(1,0,0)
        oval(
            -5+ 0 + d*step,
            height()//2,
            10,
            10
            )
    
        #print("Dot done")