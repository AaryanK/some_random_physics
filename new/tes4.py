import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

fig, ax = plt.subplots()

# Plotting the data
line1, = ax.plot(x, y1, label='Line 1', color='blue')
line2, = ax.plot(x, y2, label='Line 2', color='red')

# Adding labels
ax.set_xlabel('X-axis label')
ax.set_ylabel('Y-axis label')

# First legend in the upper right
legend1 = ax.legend(handles=[line1], loc='upper right')

# Add the first legend manually to the plot
ax.add_artist(legend1)

# Second legend in the upper left
legend2 = ax.legend(handles=[line2], loc='upper left')

plt.show()
