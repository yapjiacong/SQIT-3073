import matplotlib.pyplot as plt
import numpy as np

# Generate random data
num_points = 50
x = np.random.uniform(0, 10, num_points)
y = 3 * x + np.random.normal(0, 2, num_points)

# Fit a linear model
coeffs = np.polyfit(x, y, 1)
poly_model = np.poly1d(coeffs)

# Create the scatter plot
plt.scatter(x, y, s=50)

# Plot the regression line
x_line = np.linspace(x.min(), x.max(), 100)
y_line = poly_model(x_line)
plt.plot(x_line, y_line, 'r--')

# Show the plot
plt.show()