# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 21:35:10 2018

@author: MSG
"""

#import modules
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make  random walks, and plot the points.
# Set the size of the plotting window.
plt.figure(figsize=(10, 6))
#figure() function controls the width, height, resolution, and background
#color of the plot
while True:
    """keep making walks while program is active"""
    #walk = RandomWalk()#default 5000points
    walk = RandomWalk(50000)#set to 50000points
    walk.fill_walk()

    
    #visualize walk
    point_numbers = list(range(walk.num_points))#each point stores color
    plt.scatter(walk.x_values, walk.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=30)
    #plt.scatter(walk.x_values, walk.y_values, c=(0.63, 0.57, 0.23),  s=20)
    #mark start point
    plt.scatter(walk.x_values[0], walk.y_values[0], c=(1, 0, 0),
                edgecolor='none', s=30)
    #mark end point
    plt.scatter(walk.x_values[-1], walk.y_values[-1],  c=(0, 1, 0),
                edgecolor='none', s=50)
    #add title and axis labels
    #plt.title('Random Walk Plot by Scatter', fontsize=14, color='blue')
    #plt.xlabel('x-value', fontsize=14)
    #plt.ylabel('y-value', fontsize=14, color='green')
    #set the size of the tick lables
    #plt.tick_params(axis='both' ,labelsize=14 )
    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    #plt.show()
    
    #save plot as png image
    plt.savefig('Random_Walk-scatter_graph5.png', bbox_inches='tight')
    
    answer = input('Do you want to make another walk?: yes/no')
    answer = answer.lower()
    if answer == 'no':
        break