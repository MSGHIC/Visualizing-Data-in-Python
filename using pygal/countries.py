# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 22:23:20 2018

@author: MSG
"""
import pygal
#Pygal uses two-letter codes
from pygal.maps.world import COUNTRIES
"""Pygal’s country codes are stored in a module called i18n, short for
internationalization. The dictionary COUNTRIES contains the two-letter country
codes as keys and the country names as values. To see these codes, import
the dictionary from the i18n module and print its keys and values:"""

for country_code in sorted(COUNTRIES.keys()):
    print(country_code +' '+ COUNTRIES[country_code])