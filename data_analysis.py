#Import Libraries
#Import data
#Processs
#Visualize

import matplotlib.pyplot as plt

# Data for the graph
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]

# Create a line graph
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label='Simple Graph')

# Add labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Simple Graph Example')

# Add legend
plt.legend()

# Display the graph
plt.show()
