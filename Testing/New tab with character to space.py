# MenuTitle: New tab with character to space
# Ricard Garcia - 06.06.2019
# -------------------
# -*- coding: utf-8 -*-
__doc__="""
Creates a new tab with the selected character between all letters.
"""
# --------------------------------
from random import randint

f = Glyphs.font

# List with letters ---------------------------
letters = [
    "A",
    "B",
	"C",
	"D",
	"E",
	"F",
	"G",
	"H",
	"I",
	"J",
	"K",
	"L",
	"M",
	"N",
	"O",
	"P",
	"Q",
	"R",
	"S",
	"T",
	"U",
	"V",
	"W",
	"X",
	"Y",
	"Z"
	]
	
	
	
# Loop creating "strings" ---------------------------
outputString = ""

for g in f.selection:
	for l in letters:
		string1 = "%s%s" % (g.name, str(l))
		
		#print(string1)
	
	string2 = " "
	string2 += string1



	print(string2)
	

outputString += "%s\n" % (string2)

Font.newTab(outputString)
