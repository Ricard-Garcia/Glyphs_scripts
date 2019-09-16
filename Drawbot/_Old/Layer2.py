from GlyphsApp import *

f = Glyphs.font
masters = f.masters
layers = f.selectedLayers

#for master in f:
    #print(master)
#for g in f.selection:
#    print(g.name)
#    for layer in g.layers:
        #print(layer)
        
        
        
#print(f.familyName)
#layer = f.selection.layers[master.id]

for m in f.masters:
    #print(m.id)
    pass
    
for g in f.selection:
    for m in f.masters:
        print g.name, g.layers[m.id].name
