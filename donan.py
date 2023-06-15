import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Gravel = 1 red
# Silt = 2 blue
# Clay = 3 green
# longitude = [34.634642, 34.634652, 34.634827, 34.634711, 34.634605, 34.634210, 34.634616, 34.634652, 34.634715, 34.634740, 34.634590, 34.634617, 34.634515, 34.634966]
# latitude = [-120.480071, -120.480073, -120.479961, -120.479973, -120.480443, -120.480219, -120.479980, -120.480073, -120.480294, -120.480125, -120.480148, -120.480038, -120.480175, -120.480341]
# water_depth = [np.NaN, 60, 60, 60, 60, 60, 60, 65, 72, 65, 55, 55, 64, 56]

# Well Location DV1 data
latitude_1 = 34.634642  # Latitude for Well Location DV1
longitude_1 = -120.480071  # Longitude for Well Location DV1
depth_1 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 0, 0, 0, 0, 0, 0, 0]  # Sample depth -10
soil_data_1 = [1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 1, 1, 1, 1, 1, 1, 1]  # Soil type

# Well Location DE1 data
latitude_2 = 34.634652  # Latitude for Well Location DE1
longitude_2 = -120.480073  # Longitude for Well Location DE1
depth_2 = [0, 5, 10, 15, 20, 25, 30, 
      35, 40, 45, 50, 55, 60, 65, 0, 0, 0]  # Sample depth -14
soil_data_2 = [1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 1, 1, 1]  # Soil type
# z2 = [60]  # Water level

# Well Location DW8 data
latitude_3 = 34.634827  # Latitude for Well Location DW8
longitude_3 = -120.479961  # Longitude for Well Location DW8
depth_3 = [0, 5, 10, 15, 20, 25, 30, 
      35, 40, 45, 50, 52, 54, 55, 58, 60, 65]  # Sample depth -17
soil_data_3 = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 3]  # Soil type
# z3 = [60]  # Water level

# Well Location DW9 data
latitude_4 = 34.634711  # Latitude for Well Location DW9
longitude_4 = -120.479973  # Longitude for Well Location DVW9
depth_4 = [0, 5, 10, 15, 20, 25, 30, 35, 40,
      45, 50, 52, 54, 55, 58, 60, 65]  # Sample depth -17
soil_data_4 = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 4, 2]  # Soil type
# z4 = [60]  # Water level


# Well Location DW10 data
latitude_5 = 34.634605  # Latitude for Well Location DW10
longitude_5 = -120.480443  # Longitude for Well Location DW10
depth_5 = [0, 5, 10, 15, 20, 25, 30, 35, 40,
      45, 50, 52, 54, 55, 58, 60, 65]  # Sample depth -17
soil_data_5 = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2]  # Soil type
# z5 = [60]  # Water level


# Well Location DW11 data
latitude_6 = 34.634210  # Latitude for Well Location DW11
longitude_6 = -120.480219  # Longitude for Well Location DW11
depth_6 = [0, 5, 10, 15, 20, 25, 30, 35, 40,
      45, 50, 52, 54, 55, 58, 60, 65]  # Sample depth -17
soil_data_6 = [1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3]  # Soil type
# z6 = [60]  # Water level


# Well Location DW12 data
latitude_7 = 34.634616  # Latitude for Well Location DW12
longitude_7 = -120.479980  # Longitude for Well Location DW12
depth_7 = [0, 5, 10, 15, 20, 25, 30, 35, 40,
      45, 50, 52, 54, 55, 58, 60, 65]  # Sample depth -17
soil_data_7 = [1, 2, 2, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3]  # Soil type
# z7 = [60]  # Water level


# Well Location MW1 data
latitude_8 = 34.634652  # Latitude for Well Location MW1
longitude_8 = -120.480073  # Longitude for Well Location MW1
depth_8 = [0, 5, 10, 15, 20, 25, 30, 35, 40,
      45, 50, 55, 60, 65, 70, 75, 0]  # Sample depth 16
soil_data_8 = [1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 3, 4, 3, 3, 1]  # Soil type
# z8 = [65]  # Water level


# Well Location MW2 data
latitude_9 = 34.634715  # Latitude for Well Location MW2
longitude_9 = -120.480294  # Longitude for Well Location MW2
depth_9 = [0, 5, 10, 15, 20, 25, 30, 35, 40,
      45, 50, 55, 60, 65, 70, 75, 80]  # Sample depth 17
soil_data_9 = [1, 2, 2, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 1, 1]  # Soil type
# z9 = [72]  # Water level


# Well Location MW3 data
latitude_10 = 34.634740  # Latitude for Well Location MW3
longitude_10 = -120.480125  # Longitude for Well Location MW3
depth_10 = [0, 5, 10, 15, 20, 25, 30, 35, 40,
       45, 50, 55, 60, 65, 70, 75, 0]  # Sample depth 16
soil_data_10 = [1, 2, 2, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 4, 3, 1, 1]  # Soil type
# z10 = [65]  # Water level


# Well Location MW4 data
latitude_11 = 34.634590  # Latitude for Well Location MW4
longitude_11 = -120.480038  # Longitude for Well Location MW4
depth_11 = [0, 5, 10, 15, 20, 25, 30, 35, 40,
       45, 50, 55, 60, 65, 70, 75, 80]  # Sample depth 17
soil_data_11 = [1, 2, 3, 3, 2, 2, 2, 2, 3, 3, 4, 3, 2, 2, 3, 3, 3]  # Soil type
# z11 = [55]  # Water level


# Well Location MW5 data
latitude_12 = 34.634617  # Latitude for Well Location MW5
longitude_12 = -120.480038  # Longitude for Well Location MW5
depth_12 = [0, 5, 10, 15, 20, 25, 30, 35, 40,
       45, 50, 55, 60, 65, 0, 0, 0]  # Sample depth 14
soil_data_12 = [1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 1, 1, 1]  # Soil type
# z12 = [55]  # Water level


# Well Location MW6 data
latitude_13 = 34.634515  # Latitude for Well Location MW6
longitude_13 = -120.480175  # Longitude for Well Location MW6
depth_13 = [0, 5, 10, 15, 20, 25, 30, 35, 40,
       45, 50, 55, 60, 65, 0, 0, 0]  # Sample depth 14
soil_data_13 = [1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 4, 1, 1, 1]  # Soil type
# z13 = [64]  # Water level


# Well Location MW7 data
latitude_14 = 34.634960  # Latitude for Well Location MW7
longitude_14 = -120.480341  # Longitude for Well Location MW7
depth_14 = [0, 5, 10, 15, 20, 25, 30, 35, 40,
       45, 50, 55, 60, 65, 0, 0, 0]  # Sample depth 14
soil_data_14 = [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 1, 1, 1]  # Soil type
# z14 = [56]  # Water level

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Gravel = 1 red
# Silt = 2 blue
# Clay = 3 green
# longitude = [34.634642, 34.634652, 34.634827, 34.634711, 34.634605, 34.634210, 34.634616, 34.634652, 34.634715, 34.634740, 34.634590, 34.634617, 34.634515, 34.634966]
# latitude = [-120.480071, -120.480073, -120.479961, -120.479973, -120.480443, -120.480219, -120.479980, -120.480073, -120.480294, -120.480125, -120.480148, -120.480038, -120.480175, -120.480341]
# water_depth = [np.NaN, 60, 60, 60, 60, 60, 60, 65, 72, 65, 55, 55, 64, 56]

color_mapping = {1: 'brown', 2: 'orange', 3: 'yellow', 4: 'blue'}

# Create a list of colors corresponding to each soil type
colors = [color_mapping[number] for number in soil_data_1]
colors = [color_mapping[number] for number in soil_data_2]
colors = [color_mapping[number] for number in soil_data_3]
colors = [color_mapping[number] for number in soil_data_4]
colors = [color_mapping[number] for number in soil_data_5]
colors = [color_mapping[number] for number in soil_data_6]
colors = [color_mapping[number] for number in soil_data_7]
colors = [color_mapping[number] for number in soil_data_8]
colors = [color_mapping[number] for number in soil_data_9]
colors = [color_mapping[number] for number in soil_data_10]
colors = [color_mapping[number] for number in soil_data_11]
colors = [color_mapping[number] for number in soil_data_12]
colors = [color_mapping[number] for number in soil_data_13]
colors = [color_mapping[number] for number in soil_data_14]

# Plot Well Location DV1 labeled as o
ax.scatter([longitude_1], [latitude_1], depth_1, c=colors, marker='o', s=100)

# Plot Well Location DV1 labeled as x
ax.scatter([longitude_2], [latitude_2], depth_2, c=colors, marker='o', s=100)

# Plot Well Location DE1 labeled as h
ax.scatter([longitude_3], [latitude_3], depth_3, c=colors, marker='o', s=100)

# Plot Well Location DW9 as ,
ax.scatter([longitude_4], [latitude_4], depth_4, c=colors, marker='o', s=100)

# Plot Well Location DW10 as o
ax.scatter([longitude_5], [latitude_5], depth_5, c=colors, marker='o', s=100)

# Plot Well Location DW11 as v
ax.scatter([longitude_6], [latitude_6], depth_6, c=colors, marker='o', s=100)

# Plot Well Location DW12 as ^
ax.scatter([longitude_7], [latitude_7], depth_7, c=colors, marker='o', s=100)

# Plot Well Location MW1 as 1
ax.scatter([longitude_8], [latitude_8], depth_8, c=colors, marker='o', s=100)

# Plot Well Location MW2 as 2
ax.scatter([longitude_9], [latitude_9], depth_9, c=colors, marker='o', s=100)

# Plot Well Location MW3 as 3
ax.scatter([longitude_10], [latitude_10], depth_10, c=colors, marker='o', s=100)

# Plot Well Location MW4 as 4
ax.scatter([longitude_11], [latitude_11], depth_11, c=colors, marker='o', s=100)

# Plot Well Location MW5 as s
ax.scatter([longitude_12], [latitude_12], depth_12, c=colors, marker='o', s=100)

# Plot Well Location MW6 as p
ax.scatter([longitude_13], [latitude_13], depth_13, c=colors, marker='o', s=100)

# Plot Well Location MW7 as *
ax.scatter([longitude_14], [latitude_14], depth_14, c=colors, marker='o', s=100)

# Set labels for each axis
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Depth')
ax.invert_zaxis()

# Set the title and legend
ax.set_title('Well Locations')

# Show the 3D plot
# ax.plot_trisurf(longitude, latitude, water_depth, cmap='viridis', edgecolor='none')
plt.show()
