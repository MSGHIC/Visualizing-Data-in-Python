# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 20:30:32 2018

@author: MSG
"""
#import modules
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk, and plot the points.
walk = RandomWalk()
walk.fill_walk()

#visualize walk

plt.plot(walk.x_values, walk.y_values)
#plt.scatter(walk.x_values, walk.y_values, c=walk.y_values, cmap=plt.cm.Greys,  s=20, edgecolors=None)
#add title and axis labels
plt.title('Random Walk Plot by Scatter', fontsize=14, color='blue')
plt.xlabel('x-value', fontsize=14)
plt.ylabel('y-value', fontsize=14, color='green')
#set the size of the tick lables
plt.tick_params(axis='both' ,labelsize=14 )
#plt.show()
plt.savefig('Random_Walk-scatter_graph4.png', bbox_inches='tight')

