#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

# Random (x, y) coordinates
x = np.random.randn(2000) * 10
y = np.random.randn(2000) * 10

# Elevation value at each (x, y) point
z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

# Scatter plot with color based on elevation
scatter = plt.scatter(x, y, c=z, cmap='terrain')

# Add labels and title
plt.xlabel('x coordinate (m)')
plt.ylabel('y coordinate (m)')
plt.title('Mountain Elevation')

# Add a colorbar and label it
cbar = plt.colorbar(scatter)
cbar.set_label('elevation (m)')

# Show the plot
plt.show()
