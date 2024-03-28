import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Patch
import os
from collections import defaultdict
import matplotlib.lines as mlines
from matplotlib.font_manager import FontProperties

# Paths for CSV files and population data
path = r'C:\Users\Nathaniel L\Desktop\Coordinate CSVs\*.csv'
csv_files = glob.glob(path)

file = r'C:\Users\Nathaniel L\Downloads\data1870.csv'
population_data = pd.read_csv(file)

new_data = r'C:\Users\Nathaniel L\Downloads\data1880.csv'
new_population_data = pd.read_csv(new_data)

# Population color map
population_color_map = {
    "20000 - 30000": "darkblue",
    "15000 - 20000": "chocolate",
    "10000 - 15000": "tan",
    "5000 - 10000": "crimson",
    "2500 - 5000": "pink",
    "1000 - 2500": "gold",
    "> 1000": "darkgreen",
    "": "white",
    "nan": "white"
}

# Filtering out unnecessary keys
filtered_color_map = dict(list({k: v for k, v in population_color_map.items() if k not in ["", "nan"]}.items())[:3])
second_filtered_color_map = dict(list({k: v for k, v in population_color_map.items() if k not in ["", "nan"]}.items())[-4:])


# Creating legend handles
legend_handles = [mlines.Line2D([], [], color=color, marker='o', markeredgecolor='black',
                                linestyle='None', label=label) for label, color in filtered_color_map.items()]
second_legend_handles = [mlines.Line2D([], [], color=color, marker='o', markeredgecolor='black',
                                       linestyle='None', label=label) for label, color in second_filtered_color_map.items()]# Creating a subplot with 2 axes
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 20))
fig = plt.figure(figsize=(16, 10), facecolor='wheat')

ax1 = fig.add_axes([0.1, 0.5, 0.4, 0.45])  # Reduced height to move closer to the bottom map
ax2 = fig.add_axes([0.5, 0.05, 0.4, 0.45])  # Increased bottom to move closer to the top map

def extract_county_name(file_path):
    base_name = os.path.basename(file_path)
    county_name = base_name.split('0')[0].upper()
    return county_name

def plot_map(ax, data):
    for file in csv_files:
        dataframe = pd.read_csv(file)
        county_name = extract_county_name(file)
        population_range = data.loc[data['County'] == county_name, 'Population']
        population_range = population_range.astype(str).str.cat()
        color = population_color_map.get(population_range, "white")
        new_row = pd.DataFrame([dataframe.columns.tolist()], columns=dataframe.columns)
        dataframe = pd.concat([new_row, dataframe], ignore_index=True)
        x_coords = dataframe.iloc[:, 0].astype(float)
        y_coords = dataframe.iloc[:, 1].astype(float)
        polygon_points = list(zip(x_coords, y_coords))
        polygon_patch = Polygon(polygon_points, closed=True, facecolor=color, edgecolor='black', alpha=0.5)
        ax.add_patch(polygon_patch)


# Plotting the original data on ax1
plot_map(ax1, population_data)

# Plotting the new data on ax2
plot_map(ax2, new_population_data)

# Setting up the legend and other properties for both axes
for ax in (ax1, ax2):
    ax.autoscale()
    ax.axis('equal')
    ax.set_facecolor('wheat')
    ax.invert_xaxis()
    ax.set_xlim(86, 79)
    ax.set_ylim(30.8, 35)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

ax1.legend(handles=legend_handles, loc='upper right', bbox_to_anchor=(1.2, 0.75), fontsize=16, markerscale=6, frameon=False, labelspacing=3.5)
ax2.legend(handles=second_legend_handles, loc='upper right', bbox_to_anchor=(0.02, 0.85), fontsize=16, markerscale=6, frameon=False, labelspacing=3.5)

# Adding titles
ax1.set_title("NEGRO POPULATION OF GEORGIA BY COUNTIES .", fontdict={'weight': 'bold', 'size': 18}, y=1, x= 1)
ax1.text(0.25, 0.93, "1870", transform=ax1.transAxes, ha='center', va='bottom', fontsize=15, weight='bold')
ax2.text(0.25, 0.93, "1880", transform=ax2.transAxes, ha='center', va='bottom', fontsize=15, weight='bold')

plt.tight_layout()
plt.show()
