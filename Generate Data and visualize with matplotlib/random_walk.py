# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 19:59:15 2018

@author: MSG
"""
from random import choice

class RandomWalk():
    
    """A class to generate random walks.
    makes random decisions about which direction the walk should take."""
    def __init__(self, num_points=5000):
        """initializes a walk with 5000 points to move
        ,each with x and y coordinate"""
        self.num_points = num_points
       
        #lists to store the x- and y-coordinate values of each point in
        #the walk.
        #All the walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]
          
    def fill_walk(self):
       """fill the walk with all steps"""
       """store x and y steps"""
       # Keep taking steps until the walk reaches the desired length.
       while len(self.x_values) < self.num_points:
           next_x, next_y = self.get_step()
           self.x_values.append(next_x)
           self.y_values.append(next_y)
      
        
    def get_step(self):
       
        """Calculate all the points in the walk."""
        # Decide which direction to go and how far to go in that direction.
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        x_step = x_direction * x_distance
        
        
        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        y_step = y_direction * y_distance
        
        # Reject moves that go nowhere.
        if x_step == 0 and y_step == 0:
            #generate new x_step
            x_direction = choice([1, -1])
            x_distance = choice([1, 2, 3, 4])
            x_step = x_direction * x_distance  
            
        # Calculate the next x and y values.
        next_x = self.x_values[-1] + x_step
        next_y = self.y_values[-1] + y_step
        
                   
        return next_x, next_y
            