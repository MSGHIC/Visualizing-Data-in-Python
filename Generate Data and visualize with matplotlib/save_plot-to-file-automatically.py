# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 17:40:54 2018

@author: MSG
"""

"""Saving Your Plots Automatically
If you want your program to automatically save the plot to a file, you can
replace the call to plt.show() with a call to plt.savefig():
plt.savefig('squares_plot.png', bbox_inches='tight')
The first argument is a filename for the plot image, which will be saved
in the same directory as scatter_squares.py. The second argument trims extra
whitespace from the plot. If you want the extra whitespace around the plot,
you can omit this argument."""


# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:23:35 2018

@author: MSG
"""

import matplotlib.pyplot as plt
"""
x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
y = [12, 10, 3, 7, 20, 20, 10, 6, 7, 14]
for i in range(0, 10):
    plt.scatter(x[i], y[i], s=300, edgecolors='green')
    
#set chart title and label axes
plt.title('Scater graph', fontsize=16, color='red')
plt.xlabel('x-value' , fontsize=14)
plt.ylabel('y-value' , fontsize=14)
plt.tick_params(axis='both', which='major' ,labelsize=14 )

#show graph
plt.show()

"""
import math
#Calculating Data Automatically
x_values = list(range(1, 21))
y_values = []
for x in x_values:
    #y = math.pow(x, 2)
    y = x**2
    y_values.append(y)
#y_values = [x**2 for x in x_values]
#set range for each axis
#plt.axis([0, 1100,  1, 1100000])
#c = color
#plt.scatter(x_values, y_values, s=80, color='green')
#Values closer to 0 produce dark colors, and values closer to 1 produce
#lighter colors.
plt.scatter(x_values, y_values, s=120, c=(0.63, 0.57, 0.23))
#add title and axis labels
plt.title('Simple scatter grapgh of squared numbers 1-20', fontsize=14, color='blue')
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14, color='green')
#set the size of the tick lables
plt.tick_params(axis='both' ,labelsize=14 )
#plt.show()
plt.savefig('scatter_graph.png', bbox_inches='tight')

