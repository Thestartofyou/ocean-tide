import matplotlib.pyplot as plt
import numpy as np

# Sample tide data (replace this with real tide data)
tide_heights = np.sin(np.linspace(0, 2 * np.pi, 365))  # Example data

# Plot the tide data
plt.figure(figsize=(10, 6))
plt.plot(range(len(tide_heights)), tide_heights, label="Tide Heights")
plt.title("Novel Ocean Tide Data Visualization")
plt.xlabel("Day of the Year")
plt.ylabel("Tide Height")
plt.legend()
plt.grid(True)
plt.show()
