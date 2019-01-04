
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 21:48:05 2018

@author: MSG
"""

#import the Die class
from Die_class import Die

#create an instance of a die
die1 = Die(5)


# Make some rolls, and store results in a list.
result = []
#lets count how many times we roll each number(1-6) from both dice 
num_counts= list(range(0, die1.sides))

#roll dice at once, add score to results list,
# increment count in num_counts that matches the score got
for roll_num in range(1000):
   score1= die1.roll_die()
   result.append(score1)
   num_counts[score1-1] += 1

print('****LIST OF ALL OUTCOMES*****')
print(result)
print('*****COUNTS FOR EACH DIGIT****from 1 to '+str(die1.sides))
print(num_counts)

#lets visualize the results
import pygal

hist = pygal.Bar()
hist.title = "Results of rolling one Die6 1000 times."
hist.x_labels = list(range(1, die1.sides+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('(die1)', num_counts)
hist.render_to_file('die_visual.svg')
