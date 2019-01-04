import matplotlib.pyplot as plt
values=[1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 36]
plt.plot(values, squares, linewidth=5)

#add title and axis labels
plt.title('Simple line grapgh of squared numbers 1-6', fontsize=14, color='blue')
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14, color='green')

#set the size of the tick lables
plt.tick_params(axis='both' ,labelsize=14 )
plt.show()

