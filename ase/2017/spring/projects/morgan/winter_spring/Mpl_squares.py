
import matplotlib.pylot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth = 5)
plt.title("sqare numders", fontsize = 28)
plt.xlabel("value", fontsize = 14)
plt.ylable("squares, of value",fontsize = 14)
plt.tick_params(axis = 'both',lablesize = 14)
plt.show() 
