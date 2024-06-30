import numpy as np
import matplotlib.pyplot as plt

# Generate random data for x1 and x2
x1 = np.random.rand(1000)  # 1000 points for x1
x2 = np.random.rand(800)   # 800 points for x2

# Create histograms for x1 and x2
hist_x1, bins_x1 = np.histogram(x1, bins=30, range=(0, 1))
hist_x2, bins_x2 = np.histogram(x2, bins=30, range=(0, 1))

# Print histogram values and bin edges
print("Histogram for x1:", hist_x1)
print("Bins for x1:", bins_x1)
print("Histogram for x2:", hist_x2)
print("Bins for x2:", bins_x2)

# Compute the bin centers
bin_centers_x1 = (bins_x1[:-1] + bins_x1[1:]) / 2
bin_centers_x2 = (bins_x2[:-1] + bins_x2[1:]) / 2

# Divide the histogram counts of x1 by the histogram counts of x2
# To avoid division by zero, add a small epsilon to the denominator
epsilon = 1e-10
hist_ratio = hist_x1 / (hist_x2 + epsilon)

# Plotting the histograms and their ratio
plt.figure(figsize=(12, 6))

# Histogram for x1
plt.subplot(1, 3, 1)
plt.bar(bin_centers_x1, hist_x1, width=0.03, color='blue', alpha=0.7, label='x1')
plt.title('Histogram of x1')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# Histogram 
