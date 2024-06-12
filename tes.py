import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Example data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.sin(2 * x)

# Number of datasets
n_datasets = 4

# Create a range of colors from the 'Blues' colormap
colors_red = cm.Reds(np.linspace(0.2, 1, n_datasets))
colors_blue = cm.Blues(np.linspace(0.2, 1, n_datasets))

# Plot the datasets with different shades of red and blue
plt.figure(figsize=(10, 6))

# Plot red datasets
plt.plot(x, y1, label='sin(x) - Red', color=colors_red[0])
plt.plot(x, y2, label='cos(x) - Red', color=colors_red[1])

# Plot blue datasets
plt.plot(x, y3, label='tan(x) - Blue', color=colors_blue[0])
plt.plot(x, y4, label='sin(2x) - Blue', color=colors_blue[1])

# Adding labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Different Shades of Red and Blue for Different Datasets')

# Adding legend
plt.legend()

# Show the plot
plt.show()
