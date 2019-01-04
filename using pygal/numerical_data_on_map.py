# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 23:21:31 2018

@author: MSG
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 23:06:10 2018

@author: MSG
"""
import pygal
wm = pygal.maps.world.World()
wm.title = 'Population of Countries in North America'
wm.add('North America', {'ca': 24236120, 'mx': 42123781, 'us': 452123109})



wm.render_to_file('North America_population.svg')
