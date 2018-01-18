import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]

plt.plot(squares)



input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Set thickness of line
plt.plot(input_values, squares, linewidth = 5)

# Set chart title and labeling the axes
plt.title("Sqare Numbers", fontsize = 28)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)
# Set size of tick labels
plt.tick_params(axis = 'both', labelsize = 14)

plt.show()
