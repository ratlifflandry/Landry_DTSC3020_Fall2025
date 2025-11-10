from datascience import *
import numpy as np
import math
import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt

#Load penguins dataset from .CSV
penguins = Table.read_table('penguins.csv')

print(penguins)

species_colors = {'Adelie': 'blue', 'Chinstrap': 'green', 'Gentoo': 'red'}
colors = []
for species in penguins.column('species'):
    color = species_colors[species]
    colors.append(color)

plt.figure(figsize=(8,6))
plt.scatter(penguins.column('bill_length_mm'), penguins.column('bill_depth_mm'), c=colors)
plt.xlabel('Bill Length (mm)')
plt.ylabel('Bill Depth (mm)')
plt.title('Scatter Plot of Bill Length vs Bill Depth by Species')
plt.show()

plt.figure(figsize=(8,6))
plt.hist(penguins.column('bill_length_mm'), bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Bill Length (mm)')
plt.ylabel('Frequency')
plt.title('Histogram of Bill Length (10 bins)')
plt.show()

plt.figure(figsize=(8,6))
plt.hist(penguins.column('bill_length_mm'), bins=30, color='salmon', edgecolor='black')
plt.xlabel('Bill Length (mm)')
plt.ylabel('Frequency')
plt.title('Histogram of Bill Length (30 bins)')
plt.show()

species_list = np.unique(penguins.column('species'))

data = []
for species in species_list:
    body_mass = penguins.where('species', species).column('body_mass_g')
    data.append(body_mass)

plt.figure(figsize=(8,6))
plt.boxplot(data, labels=species_list)
plt.ylabel('Body Mass (g)')
plt.title('Boxplot of Body Mass by Species')
plt.show()