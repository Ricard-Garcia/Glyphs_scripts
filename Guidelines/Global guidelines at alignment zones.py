# MenuTitle: Guides through all alignment zones
# Ricard Garcia - 05.11.2018
# -------------------
# -*- coding: utf-8 -*-
__doc__="""
Sets a global guideline in each alignment zone.
"""


# For each alignment zone in the current master
for az in Font.masters[0].alignmentZones:

	# Get alignment zone position + its size
	AlignZone = az.position + az.size
	guidelineOrigin = (0, AlignZone)

	# Set the variable for the guideline
	myGuideline = GSGuideLine()
	# Add position
	myGuideline.position = guidelineOrigin

	# Set the variable
	thisMaster = Font.selectedFontMaster
	# Add position
	thisMaster.addGuideLine_( myGuideline )

	print ("Guidelines are now at: %d"%AlignZone)


Glyphs.showNotification("Guidelines", "Global guidelines set at alignment zones.")