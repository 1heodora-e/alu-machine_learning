#!/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Load data and labels
lib = np.load("pca.npz")
data = lib["data"]
labels = lib["labels"]

# Normalize data by subtracting the mean
data_means = np.mean(data, axis=0)
norm_data = data - data_means

# Apply SVD for PCA
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with colors based on labels
scatter = ax.scatter(
    pca_data[:, 0],  # U1
    pca_data[:, 1],  # U2
    pca_data[:, 2],  # U3
    c=labels,
    cmap='plasma'
)

# Axis labels
ax.set_xlabel("U1")
ax.set_ylabel("U2")
ax.set_zlabel("U3")

# Title
plt.title("PCA of Iris Dataset")

# Show plot
plt.show()
