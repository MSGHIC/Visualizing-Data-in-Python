# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 17:26:26 2018

@author: MSG
"""
import matplotlib.pyplot as plt
"""color maps
A colormap is a series of colors in a gradient that moves from a starting to
ending color. Colormaps are used in visualizations to emphasize a pattern
in the data. For example, you might make low values a light color and high
values a darker color."""



import math
#Calculating Data Automatically
x_values = list(range(1, 21))
y_values = []
y_values = [x**2 for x in x_values]
#plot and apply color map
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Oranges,
edgecolor='none', s=140)
"""We pass the list of y-values to c and then tell pyplot which colormap to
use through the cmap argument. This code colors the points with lower
y-values light blue and the points with larger y-values dark blue."""
#add title and axis labels
plt.title('Simple scatter grapgh of squared numbers 1-20', fontsize=14, color='blue')
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14, color='green')
#set the size of the tick lables
plt.tick_params(axis='both' ,labelsize=14 )
plt.show()
