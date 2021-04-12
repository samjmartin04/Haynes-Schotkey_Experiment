# Importing Modules:

# Numpy is a module for scientific computing, shortened to 'np'.
import numpy as np
from math import sqrt
from scipy.optimize import curve_fit
# Matplotlib is for plotting
# This next line is kinda weird, we use it to make plots showup nicely in the notebook.
#Don't worry about this too much.

# This line allows us to type plt, not matplotlib.pyplot, as we are lazy!
from matplotlib import pyplot as plt

# Peter-i-fy your graph:
from matplotlib import rcParams
rcParams['xtick.direction'] = 'in'      # x-axis ticks face inwards
rcParams['ytick.direction'] = 'in'      # y-axis ticks face inwards
rcParams['xtick.top'] = True            # x-axis ticks on top
rcParams['ytick.right'] = True          # y-axis ticks on right
rcParams['errorbar.capsize'] = 3
rcParams['lines.markersize'] = 8       # Data point size
rcParams['figure.figsize'] = 8, 5

rcParams['xtick.major.size'] = 6
rcParams['xtick.major.width'] = 1.5
rcParams['ytick.major.size'] = 6
rcParams['ytick.major.width'] = 1.5

rcParams['axes.linewidth'] = 1.5        # line thickness of the axes
rcParams['axes.labelsize'] = 16         # Size of axis labels
rcParams['font.size'] = 16

# https://matplotlib.org/3.1.1/tutorials/introductory/customizing.html - for more customisation.

def clean_data(col1, col2, col3):
    n = 0
    while n < len(col2):
        if col2[n] <= 4:
            if col2[n+1] > 4:
                injection_time = n
                print(injection_time)
                break
        n += 1
    col1 = col1[injection_time:len(col1)-100]
    col3 = col3[injection_time:len(col3)-100]
    col1 = col1 - col1[0]

    n = 0
    while n < len(col1):
        if col1[n] >= 0.95e-6:
            neat_data_point = n
            break
        n += 1

    col1 = col1[neat_data_point:]
    col3 = col3[neat_data_point:]
    return col1*10**6, col3*10**3

# Loading data from a .csv

# Data will be loaded from a .csv file using np.loadtxt()
# Comma for each separate array of columns
column1, column2, column3 = np.loadtxt('Data/C1 6V.csv', delimiter=',', unpack=True)
x1, y1 = clean_data(column1, column2, column3)

#column1, column3 = np.loadtxt('Data/Random Walk with Low Temperature.csv', delimiter=',', unpack=True)
#x2, y2 = column1, column3

A = 0.000102
D = 0.000555
tau = 6.02*10**-7
v = 94.34
mu = 0.0149
pi = 3.14
t = x1

#fit = A*1/sqrt(4*pi*D*t)*np.exp(-(x-v*t)**2/4*D*t)*np.exp(-t/tau)



popt, pcov = curve_fit(fit_fun, x1, y1)
print(popt)

plt.figure(dpi=300) # Used with the saving to improve the quality of the saved image

# the yerr input is the standard error on y
# the fmt input sets the format '.' for points, 'x' for crosses, '-' for a line. Letter is colour
a = plt.plot(x1, y1, 'k.')    # So this is y against x with y error bars from 'y_err' data, with black dots.
#a = plt.plot(x2, y2, 'b.')

plt.ylabel("Electrical Bias")
plt.xlabel("Time")

#plt.show()
plt.gca().set_aspect(0.00075)

#plt.savefig('Report/Graph.png') # Save the graph for a higher quality image

#x_range_lower = -0.05
#x_range_higher = 1.25       # Set x range limits here to adjust the plot with them and for the best fit line stuff below.
