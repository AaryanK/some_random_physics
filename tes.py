import numpy as np
import matplotlib.pyplot as plt

# Sample data
list1 =np.random.rand(8)
list2 =np.random.rand(10)
list3 = np.divide(list1,list2)
print(list1)
print(list2)
print(list3)
# list2 = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]

# Create histograms
hist1, bin_edges1 = np.histogram(list1, bins=4)
hist2, bin_edges2 = np.histogram(list2, bins=4)

# Element-wise division of histograms
hist_division = np.divide(hist1, hist2, out=np.zeros_like(hist1, dtype=float), where=hist2!=0)

# Plotting the histograms
fig, axs = plt.subplots(3, 1, figsize=(10, 8))

# Plot histogram 1
axs[0].plot(list1)
axs[0].set_title('Histogram 1')
axs[0].set_xlabel('Bins')
axs[0].set_ylabel('Counts')

# Plot histogram 2
axs[1].plot(list2)
axs[1].set_title('Histogram 2')
axs[1].set_xlabel('Bins')
axs[1].set_ylabel('Counts')

# Plot divided histogram
# We use the bin edges from the first histogram for consistency
axs[2].plot(list3)
axs[2].set_title('Divided Histogram (Histogram 1 / Histogram 2)')
axs[2].set_xlabel('Bins')
axs[2].set_ylabel('Division Result')

plt.tight_layout()
plt.show()
