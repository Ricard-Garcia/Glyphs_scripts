# MenuTitle: Add notes
# Ricard Garcia 29.08.2019
# -------------------
# -*- coding: utf-8 -*-
__doc__="""
Adds a string to the notes tab in font info.
"""

# Accessing the font
font = Glyphs.font

# String to append
stringToAppend = "This is a testing string"

# Adding the string
font.note = stringToAppend

# Printing the notes
print(font.note)