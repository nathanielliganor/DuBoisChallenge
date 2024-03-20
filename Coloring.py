import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import os
from collections import defaultdict

path = r'C:\Users\Nathaniel L\Desktop\Coordinate CSVs\*.csv'  # Note the use of raw string and *.csv to match all CSV files
csv_files = glob.glob(path)

file = r'C:\Users\Nathaniel L\Downloads\data1870.csv'
population_data = pd.read_csv(file)

# Pandas DataFrame
print(population_data)

fig, ax = plt.subplots()

population_color_map = {
    "20000 - 30000": "blue",
    "15000 - 20000": "brown",
    "10000 - 15000": "gray",
    "5000 - 10000": "red",
    "2500 - 5000": "pink",
    "1000 - 2500": "yellow",
    "> 1000": "green"
}

def extract_county_name(file_path):
    # Example function to extract the county name from the file path
    base_name = os.path.basename(file_path)
    # Isolates county name
    county_name = base_name.split('0')[0].upper()
    return county_name

print(csv_files)

for file in csv_files:
    dataframe = pd.read_csv(file)
    # Assuming the function extract_county_name correctly extracts the county name from your CSV file name
    county_name = extract_county_name(file)
    # Find the population range for this county
    # population_range = population_data.loc[population_data['County'] == county_name, 'Population'].values[0]

    # Does not account for the duplicates yet
    population_range = population_data.loc[population_data['County'] == county_name, 'Population']
    population_range = population_range.astype(str).str.cat()
    # Panda Series Type
    print(population_range)

    # Get the corresponding color
    # color = population_color_map[population_range]

'''
    # Add column coordinates to the rest of the coordinates
    new_row = pd.DataFrame([dataframe.columns.tolist()], columns=dataframe.columns)
    new_frame = pd.concat([new_row, dataframe], ignore_index=True)

    # Extracting x and y coordinates
    x_coords = new_frame.iloc[:, 0].astype(float)
    y_coords = new_frame.iloc[:, 1].astype(float)

    # Creating a list of (x, y) tuples for the polygon
    polygon_points = list(zip(x_coords, y_coords))

    # Create a polygon patch with the polygon vertices and set its color based on the population range
    polygon_patch = Polygon(polygon_points, closed=True, facecolor=color, edgecolor='black', alpha=0.5)

    # Add the patch to the axes
    ax.add_patch(polygon_patch)

ax.autoscale()
ax.axis('equal')
plt.show()
'''