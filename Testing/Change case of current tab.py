# MenuTitle: Text's case changer
# Ricard Garcia - 19.04.2018
# -------------------
# -*- coding: utf-8 -*-
__doc__="""
Changes case (upper, lower, titling) of the text in current tab.
"""

# ---------------------
# Modules
from GlyphsApp import *
from vanilla import *

# ---------------------
# General variables
f = Glyphs.font
glyphs = f.glyphs
tabs = f.tabs


class caseChanger(object):

	if tabs > 0:
		def __init__(self):
		
			self.w = FloatingWindow((180, 90), "Change case of text")
			self.w.UCButton = Button((10, -80, -10, 20), "Uppercase", callback=self.upperCallback)
			self.w.lcButton = Button((10, -55, -10, 20), "Lowercase", callback=self.lowerCallback)
			self.w.titleButton = Button((10, -30, -10, 20), "Title", callback=self.titleCallback)
		
			self.w.open()

		# Uppercase
		def upperCallback(self, sender):
			f.currentText = f.currentText.upper()
			
		# Lowercase
		def lowerCallback(self, sender):
		 	f.currentText = f.currentText.lower()
		
		# Title
		def titleCallback(self, sender):
		 	f.currentText = f.currentText.title()
			
	else:
			Message("No tabs", "Please, create a new tab with text in it.", OKButton=None)	


caseChanger()