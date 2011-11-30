Hungarian hyphenation patterns with non-standard hyphenation patch
------------------------------------------------------------------
Patch version: 2006-12-13

Language: Hungarian (hu HU)
Origin:   http://www.tipogral.hu/ 
License:  GPL v2 license, 2006
Author:   Nagy Bence <gimb (at) freemail (dot) hu>
Version:  v20060713
Patch:    László Németh <nemeth (at) OOo>
          source: http://sourceforge.net/project/magyarispell (OOo huhyphn)
          license: MPL/GPL/LGPL

hyph_hu_HU.dic: Unicode version, for min. OpenOffice.org 2.1
hyph_hu_HU_nonutf: ISO8859-2 version, for older OpenOffice.orgs, Scribus etc.

Installation: put the following line to the dictionary.lst file of
OpenOffice.org distribution, and copy the hyph_hu_HU.dic file to
the directory of dictionary.lst (for example, .openoffice.org2/user/wordbook
on Linux):

HYPH hu HU hyph_hu_HU

or use File->Wizards->Install new dictionaries
with online installation, or download the Hungarian pack file
from http://wiki.services.openoffice.org/wiki/dictionaries and install
offline.

The most complete collection of hyphenation patterns for TeX, OpenOffice.org
and all programs using the LibHnj library.
