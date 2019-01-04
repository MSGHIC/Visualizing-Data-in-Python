# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 23:06:10 2018

@author: MSG
"""
import pygal
wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn','cu', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl',  'co', 'ec', 'gf',
'gy', 'pe', 'py', 'sr', 'uy', 've'])


wm.render_to_file('americas.svg')
