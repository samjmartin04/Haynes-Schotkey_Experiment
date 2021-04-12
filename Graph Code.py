# Importing Modules:

# Numpy is a module for scientific computing, shortened to 'np'.
import numpy as np

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

rcParams['axes.linewidth'] = 0.6        # line thickness of the axes
rcParams['axes.labelsize'] = 13         # Size of axis labels

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
column1, column2, column3 = np.loadtxt('Data/B C3 Low T.csv', delimiter=',', unpack=True)
x1, y1 = clean_data(column1, column2, column3)

column1, column2, column3 = np.loadtxt('Data/D C3 High T.csv', delimiter=',', unpack=True)
x2, y2 = clean_data(column1, column2, column3)



plt.figure(dpi=300) # Used with the saving to improve the quality of the saved image

# the yerr input is the standard error on y
# the fmt input sets the format '.' for points, 'x' for crosses, '-' for a line. Letter is colour
a = plt.plot(x1, y1, 'b.')    # So this is y against x with y error bars from 'y_err' data, with black dots.
a = plt.plot(x2, y2, 'r.')

plt.ylabel("Voltage / mV")
plt.xlabel("Time / μs")

#plt.xlim(0, 1.4)        # x range of data
#plt.ylim(-70, 75)    # y range of data

#plt.gca().set_aspect(0.075) # Used to get a square graph - this value is range of xlim/range of ylim (here (1030-400)/(51-0))

#plt.show()

plt.savefig('Temperature Graph.png') # Save the graph for a higher quality image

x_range_lower = -0.05
x_range_higher = 1.25       # Set x range limits here to adjust the plot with them and for the best fit line stuff below.
