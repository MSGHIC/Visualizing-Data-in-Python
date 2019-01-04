# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 23:38:44 2018

@author: MSG
"""
import pygal
import csv
from datetime import datetime
#filename = 'sitka_weather_07-2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    #create a reader object
    reader = csv.reader(f)
    #get next line in the file 
    #gets the first line of the file, which contains the file headers
    header_row = next(reader)
    #print(header_row)
        
    #We use enumerate() on the list to get the index of each item, as well
    #as the value.
    for index, column_header in enumerate(header_row):
        print(index, column_header)
        
    #Extracting and Reading Data
    
   # Get dates ,low and high temperatures from file.
    dates, high_temps, low_temps = [], [], []
    for row in reader:
    #Because we’ve already read the header row, the loop will begin
    #at the second line where the actual data begins
        try:
            #convert the strings to integers(to allow visualisation)
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])  
            low  = int(row[2]) 
    
        except ValueError:
            #pass
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            high_temps.append(high)
            low_temps.append(low)
        
    print('high_temps')
    print(high_temps)
    print(' ')
    print('low_temps')
    print(low_temps)

#visualize results
import matplotlib.pyplot as plt

fig = plt.figure(dpi=80, figsize=(10, 6))
#shade areas in the plot
#use the fill_between() method, which takes a series of x-values and two
#series of y-values, and fills the space between the two y-value series
#alpha controls the color's transparency 
plt.plot(dates, high_temps, c='red', alpha=0.6)
plt.plot(dates, low_temps, c='blue', alpha=0.5)
plt.fill_between(dates, high_temps, low_temps, facecolor='blue', alpha=0.1)
fig.autofmt_xdate()


# Format plot.
plt.title('Monthly high,and low temperatures, \n Death_valley 2014', fontsize=24)
plt.xlabel(' ')
plt.ylabel('Temperature (F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
#plt.savefig('weather_temp.svg')
plt.savefig('weather_temp.png')
plt.show()