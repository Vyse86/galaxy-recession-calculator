import matplotlib.pyplot as plt # Matplotlib's plotting intervace, aliased as plt
import numpy as np # Numpy for efficient array operations

Ho = 70 
# Generate 500 evenly spaced distance values from 1 to 1000 Megaparsecs
distances = np.linspace(1, 1000, 500)
# Apply Hubble's Law to entire array at once (vectorization - no loop needed)
speeds = Ho * distances
plt.style.use('dark_background')
plt.figure(figsize = (10, 6)) # Create a figure window, 10 inches wide by 6 inches tall
plt.plot(distances, speeds, color = 'cyan', linewidth = 2) # Draw the Hubble line
plt.title("Hubble's Law - Galaxy Recession Speed vs Distance") # Graph title
plt.xlabel("Distance (Megaparsecs)") # Label for X axis
plt.ylabel("Recession Speed (km/s)") # Label for y axis
plt.grid(True) # Add a background grid for readability
plt.tight_layout() # Automatically adjust spacing so nothing gets cut off

# Real galaxy data: [distance in Mpc, recession speed in km/s]
galaxies = { 
    "Andromeda": (0.78, 54),
    "Virgo Cluster": (16.5, 1155),
    "Coma Cluster": (99, 6853),
    "Hydra Cluster": (200, 14000)
}
for name, (d, v) in galaxies.items():
    plt.scatter(d, v, color = 'red', zorder = 5, s = 50) # plot the dot, red dots size 50
    plt.annotate(name, (d, v), textcoords = "offset points",
                 xytext = (10, 5), color = 'white', fontsize = 8) # label it

plt.savefig('hubble.png', dpi = 300)
plt.show() # Render and display the plot window



