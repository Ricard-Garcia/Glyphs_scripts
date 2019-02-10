#MenuTitle: Font info data
# -*- coding: utf-8 -*-
'''
	Set font.info data to Current font.
'''

#Glyphs
from robofab.world import CurrentFont


font = CurrentFont()

# font.info.xxxxxxxxxxxxxx = data

# ------ Imprimir ------
print font.info.familyName
print font.info.styleName
print font.info.versionMajor
print font.info.versionMinor

print font.info.copyright
print font.info.trademark

# ------ Assignat ------
font.info.familyName = "Nom tipografia"
font.info.styleName = "Estil"
font.info.versionMajor = 1
font.info.versionMinor = 001
font.info.year = 2017

font.info.copyright = u"(c) Ricard Garcia"    #La "u" davant és per especificar que no hi hagi problemes amb símbols com ©
font.info.trademark = "Marca"


print "Done!"
