# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 22:16:07 2018

@author: MSG
"""

#import the Die class
from Die_class import Die

#create an instance of a die
die1 = Die(6)
die2 = Die(6)

# Make some rolls, and store results in a list.
result = []
sum_of_sides = die1.sides+die2.sides
#lets count how many times we roll each number(1-6) from both dice 
num_counts= list(range(0, sum_of_sides-1))
#num_counts = []
#roll dice at once, add score to results list,
# increment count in num_counts that matches the score got
for roll_num in range(10000):
    #compute sum of the scores from after rolling dice
   sum_score = die1.roll_die()+die2.roll_die()
   result.append(sum_score)
   num_counts[sum_score-2] += 1
#for value in range(2, sum_of_sides+1):
    #frequency = result.count(value)
    #num_counts.append(frequency)

print('****LIST OF ALL OUTCOMES*****')
print(result)
print('*****COUNTS FOR EACH DIGIT****from 1 to '+str(sum_of_sides))
print(num_counts)

#lets visualize the results
import pygal

hist = pygal.Bar()
hist.title = "Results of rolling  Dice 1000 times."
hist.x_labels = list(range(2, sum_of_sides+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('(die1+die2)', num_counts)
hist.render_to_file('dice_visual.svg')
