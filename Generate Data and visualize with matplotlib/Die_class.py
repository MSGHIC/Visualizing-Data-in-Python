# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 20:49:24 2018

@author: MSG
"""

from random import randint

class Die():
    """A class representing a single die"""
    def __init__(self, sides=6):
        #die constructor
        """Assumes a 6 sided die"""
        self.sides = sides
    
    
    def roll_die(self, times=1):
        """rolls a die a given number of times and 
        Returns a random value between 1 and number of sides."""
        for i in range(1, times+1):
            outcome = randint(1, self.sides)
        return outcome
    