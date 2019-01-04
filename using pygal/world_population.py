# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 18:36:56 2018

@author: MSG
"""
#import module to read file
import json

filename = 'population_data.json'

#Pygal uses two-letter codes
from country_codes import get_country_code


#load the data into a list
with open(filename) as f:
    popu_data = json.load(f)
 
#Build a dictionary of population data.
#Grouping Countries by Population
#three population levels:
# lessthan 10 million, between 10 million and 1 billion, and more than 1 billion
populations_L10M = {}
populations_B10M_1B = {}
populations_1Bplus = {}

# Print the 2010 population for each country.
for popu_dict in popu_data:
    if popu_dict['Year'] == '2010':
        #convert population string to int, taking care of decimals
        population = int(float(popu_dict['Value']))
        country = popu_dict['Country Name']
        code = get_country_code(country)
        #we consider only countries with code in the world map
        if code:
            if population < 10000000:
                populations_L10M[code] = population
            elif population < 1000000000:
                populations_B10M_1B[code] = population
            else:
                populations_1Bplus[code] = population
            
            print('Country Name:'+country +
                  '  Country Code :'+ str(code) +
                  '  Population :'+str(population))   
            print(" ")
        else:
            print('ERROR: '+country)
#Building a World Map

import pygal
#styling pygal...coloring
#from pygal.style import RotateStyle
#wm_style = RotateStyle('#336625')
#wm = pygal.maps.world.World(style=wm_style)
#no change noted

wm = pygal.maps.world.World()
wm.title = 'Population of Countries in the World (2010)'
wm.add('Less than 10Million', populations_L10M)
wm.add('Between 10Million to 1 Billion', populations_B10M_1B)
wm.add('Over 1 Billion', populations_1Bplus)



wm.render_to_file('World Population(2010).svg')
