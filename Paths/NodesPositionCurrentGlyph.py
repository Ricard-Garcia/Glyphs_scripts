# MenuTitle: Nodes' positions in current glyph
# Ricard Garcia 29.08.2019
# -------------------
# -*- coding: utf-8 -*-
__doc__="""
Prints the position of each node in the current glyph.
"""

# Accessing the current font
font = Glyphs.font
# Active layer
layer = font.selectedLayers[0]

# Loop to iterate through nodes in each path.
for i, path in enumerate(layer.paths):
	#print(i, path)
	
	for i, node in enumerate(path.nodes):
		print(i, node.position)
		print(i, node.type)
		print("this is the previous point position:", path.nodes[i-1])