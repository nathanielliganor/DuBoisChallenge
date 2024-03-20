import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# CSV Files 2-6
# Path to the folder containing your CSV files
path = r'C:\Users\Nathaniel L\Desktop\Coordinate CSVs\*.csv'
csv_files = glob.glob(path)

dataframes = [pd.read_csv(file) for file in csv_files]

# Dataframes is a List Type
# print(dataframes)

# List of new dataframes with all coordinates together
new_dataframes = []
for dataframe in dataframes:
    # Adds column coordinates to the rest of the coordinates
    new_row = pd.DataFrame([dataframe.columns.tolist()], columns=dataframe.columns)
    new_frame = pd.concat([new_row, dataframe], ignore_index=True)
    # Adds dataframe into new list
    new_dataframes.append(new_frame)

# This is a list
# print(new_dataframes)

fig, ax = plt.subplots()

for dataframe in new_dataframes:
    # Extracting x and y coordinates
    x_coords = dataframe.iloc[:, 0].astype(float)
    y_coords = dataframe.iloc[:, 1].astype(float)

    # Creating a list of (x, y) tuples for the polygon
    polygon_points = list(zip(x_coords, y_coords))

    # Create a polygon patch with the polygon vertices
    polygon_patch = Polygon(polygon_points, closed=True, facecolor='blue', edgecolor='black', alpha=0.5)

    # Add the patch to the axes
    ax.add_patch(polygon_patch)

ax.autoscale()
ax.axis('equal')  # Optionally, set the aspect ratio equal to make the plot isotropic
plt.show()