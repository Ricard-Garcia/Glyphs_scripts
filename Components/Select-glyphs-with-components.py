#MenuTitle: Select glyphs that contain at least one component.
# -*- coding: utf-8 -*-
__doc__="""
In current font and frontmost layer, select all glyphs with a component in it.
"""

# Acessing the font
f = Glyphs.font

# Empty list used to append glyphs with components
selection = []

# Loop of glyphs inside the font
for g in f.glyphs:
	# Accessing the current master layer
	layer = g.layers[f.selectedFontMaster.id]
	#print("First loop")

	# If there are components in the g.layer
	if len(layer.components) > 0:
		# Append current glyph to "selection"
		selection.append(g)
		#print(g.name, "has component")
		
	else:
		#print(g.name, "doesn't have components")
		continue

# Printing each element in the list "selection"
# for g in selection:
# 	print(g)		

# Setting font selection to the list "selection"
f.selection = selection