import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
data1 = np.random.rand(10, 12)  # Random data for first heatmap
data2 = np.random.rand(10, 12)  # Random data for second heatmap

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot the first heatmap (blue colormap)
heatmap1 = ax1.imshow(data1, cmap='Blues')
ax1.set_title('Heatmap 1 (Blue Colormap)')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
fig.colorbar(heatmap1, ax=ax1, orientation='vertical')

# Plot the second heatmap (red colormap)
heatmap2 = ax2.imshow(data2, cmap='Reds')
ax2.set_title('Heatmap 2 (Red Colormap)')
ax2.set_xlabel('X axis')
ax2.set_ylabel('Y axis')
fig.colorbar(heatmap2, ax=ax2, orientation='vertical')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
