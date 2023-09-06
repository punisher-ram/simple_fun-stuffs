import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()

# Draw the heart shape
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * (np.sin(t)**3)
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
ax.plot(x, y, color='red')

# Display the message "I Love You" inside the heart
ax.text(0, -4, "by punisher", fontsize=12, color='red', ha='center')

# Set aspect ratio and remove axes
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

# Show the plot
plt.show()
