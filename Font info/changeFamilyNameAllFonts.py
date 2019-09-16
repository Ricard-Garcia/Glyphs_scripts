# MenuTitle: Change family name in all fonts
# Ricard Garcia - 19.05.2019
# -------------------
# -*- coding: utf-8 -*-
__doc__="""
In all opened fonts, changes family name with the one written in the window.
"""

# Modules
from GlyphsApp import *
from vanilla import *


class changeFamilyName(object):

	def __init__(self):
		
		
		font = Glyphs.font
		
		
		self.w = FloatingWindow((250, 70), "Change family name")
		self.w.label = TextBox((10, 10, -120, 20), "FamilyName:")
		self.w.newFamilyName = EditText((-130, 10, -10, 20),  "%s"%(font.familyName), sizeStyle='small')
		self.w.createButton = Button((10, -30, -10, 20), "Add Name", callback=self.buttonCallback)
	
		self.w.open()

	def buttonCallback(self, sender):
		fonts = Glyphs.fonts
		for f in fonts:
			f.familyName = self.w.newFamilyName.get()
		
		self.w.close()
	

changeFamilyName()