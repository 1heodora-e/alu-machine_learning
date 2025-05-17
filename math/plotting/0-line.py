#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# y = x^3 from x = 0 to 10
y = np.arange(0, 11) ** 3

# Create x values from 0 to 10 (same length as y)
x = np.arange(0, 11)

# Plot with a solid red line ('r-' means red solid line)
plt.plot(x, y, 'r-')

# Show the plot
plt.show()
