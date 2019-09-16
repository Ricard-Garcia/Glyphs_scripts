# MenuTitle: Generate a sample string for numbers
# Ricard Garcia 29.08.2019
# -------------------
# -*- coding: utf-8 -*-
__doc__="""
Generates a sample string for spacing numbers.
"""

# --------------------
# Modules
from AppKit import *
from GlyphsApp import *
from vanilla import *

# ---------------------
# General variables
f = Glyphs.font
glyphs = f.glyphs
tabs = f.tabs


# Vanilla window
class lowercaseOrUppercase(object):

	def __init__(self):
		
		self.w = FloatingWindow((250, 60), "Number spacing strings")
		self.w.UCButton = Button((10, -55, -10, 20), "Uppercase", callback=self.upperCallback)
		self.w.lcButton = Button((10, -30, -10, 20), "Lowercase", callback=self.lowerCallback)
		
		self.w.open()

	
	# Copy to clipboard function
	def setClipboard( myText ):
		"""
		Sets the contents of the clipboard to myText.
		Returns True if successful, False if unsuccessful.
		"""
		try:
			myClipboard = NSPasteboard.generalPasteboard()
			myClipboard.declareTypes_owner_( [NSStringPboardType], None )
			myClipboard.setString_forType_( myText, NSStringPboardType )
			return True
		except Exception as e:
			return False

	if not setClipboard("clipboard text"):
		print "Warning: could not set clipboard to %s" % ( "clipboard text" )


	# Uppercase button
	def upperCallback(self, sender):

		# ------------------------------------------------------------

		# Empty string to append generated text
		tabText = ""

		# List of numbers
		numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

		# ------------------------------------------------------------


		for n in numbers:
			line2Append = "%sHH%sHOHO%sOO\n" % (n, n, n)
			tabText += line2Append

		# Copy to clipboard
		setClipboard(tabText)	

		# New tab
		Font.newTab(tabText)

		# Floating notification:
		Glyphs.showNotification( 
			u"%s" % (f.familyName),
			u"Uppercase/Number spacing string to clipboard.",
			)
			

	# Lowercase button
	def lowerCallback(self, sender):

		# ------------------------------------------------------------

		# Empty string to append generated text
		tabText = ""

		# List of numbers
		numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

		# ------------------------------------------------------------

		for n in numbers:
			line2Append = "%snn%snono%soo\n" % (n, n, n)
			tabText += line2Append

		# Copy to clipboard
		setClipboard(tabText)	

		# New tab
		Font.newTab(tabText)

		# Activate oldstyle figures 
		f.currentTab.features = ['onum']

		# Floating notification:
		Glyphs.showNotification( 
			u"%s" % (f.familyName),
			u"Lowercase/Number spacing string to clipboard.",
			)
			
			
# Calling the class
lowercaseOrUppercase()