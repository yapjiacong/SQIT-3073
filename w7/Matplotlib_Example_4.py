import matplotlib.pyplot as plt
import numpy as np

# Generate random data
num_points = 50
x = np.random.uniform(0, 10, num_points)
y = np.random.uniform(0, 10, num_points)
colors = np.random.uniform(0, 1, num_points)

# Create the plot
plt.scatter(x, y, s=100, c=colors, marker='o')

# Show the plot
plt.show()
