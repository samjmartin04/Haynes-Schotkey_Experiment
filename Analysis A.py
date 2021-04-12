# Importing Modules:

# Numpy is a module for scientific computing, shortened to 'np'.
import numpy as np
import pandas as pd
import os
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
rcParams['lines.markersize'] = 20       # Data point size
rcParams['figure.figsize'] = 8, 5

rcParams['xtick.major.size'] = 6
rcParams['xtick.major.width'] = 1.5
rcParams['ytick.major.size'] = 6
rcParams['ytick.major.width'] = 1.5

rcParams['axes.linewidth'] = 1.5        # line thickness of the axes
rcParams['axes.labelsize'] = 18         # Size of axis labels
rcParams['font.size'] = 18

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
sheets = ["C3 10 V", "C3 9.5 V", "C3 9 V", "C3 8.5 V", "C3 8 V", "C3 7.5 V", "C3 7 V", "C3 6.5 V", "C3 6 V", "C3 5.5 V", "C3 5 V", "C3 4.5 V", "C3 4 V"]
#sheets = ["C2 10 V"]
if False:
    for sheet in sheets:
        df = pd.read_excel("Data/C3 High Temp.xls", sheet_name=sheet)
        output = [[0, 0, 0]]
        n = 1
        while n < len(df.index):
            row = [int(df.loc[n].at['X'])*5*10**-9, df.loc[n].at['CH1'], df.loc[n].at['CH2']]
            output.append(row)
            n += 1
        output = output[1:]
        print("Saving temp csv")
        pd.DataFrame(output).to_csv("Data/temp.csv", header=None, index=None)
        column1, column2, column3 = np.loadtxt('Data/temp.csv', delimiter=',', unpack=True)
        os.remove("Data/temp.csv")
        x2, y2 = clean_data(column1, column2, column3)
        output = [[0,0]]
        n = 0
        while n < len(x2):
            row = [x2[n], y2[n]]
            output.append(row)
            n += 1
        output = output[1:]
        pd.DataFrame(output).to_csv(f"Data/C3 High Temp/{sheet}.csv", header=None, index=None)

if True:
    Vs = [10, 9.5, 9, 8.5, 8, 7.5, 7, 6.5, 6, 5.5, 5, 4.5, 4]
    inverse_V = []
    for V in Vs:
        inverse_V.append(1000/V)
    max_V_times1 = []
    times_error1 = []
    for sheet in sheets:
        column1, column2 = np.loadtxt(f'Data/C3 All Voltages/{sheet}.csv', delimiter=',', unpack=True)
        x1, y1 = column1, column2
        max_V = 0
        n = 0
        while n < len(y1):
            if y1[n] > max_V:
                max_V = y1[n]
                max_V_index = n
            n += 1
        equal_V = []
        n = 0
        while n < len(y1):
            if y1[n] == max_V:
                equal_V.append(x1[n])
            n += 1
        print(len(equal_V))
        if len(equal_V) > 1:
            av = (equal_V[0]+equal_V[-1])/2
            error = (av-equal_V[0])
        time = x1[max_V_index]
        time_error = error
        max_V_times1.append(time)
        times_error1.append(time_error)

    max_V_times2 = []
    times_error2 = []
    for sheet in sheets:
        column1, column2 = np.loadtxt(f'Data/C3 High Temp/{sheet}.csv', delimiter=',', unpack=True)
        x1, y1 = column1, column2
        max_V = 0
        n = 0
        while n < len(y1):
            if y1[n] > max_V:
                max_V = y1[n]
                max_V_index = n
            n += 1
        equal_V = []
        n = 0
        while n < len(y1):
            if y1[n] == max_V:
                equal_V.append(x1[n])
            n += 1
        print(len(equal_V))
        if len(equal_V) > 1:
            av = (equal_V[0]+equal_V[-1])/2
            error = (av-equal_V[0])
        time = x1[max_V_index]
        time_error = error
        max_V_times2.append(time)
        times_error2.append(time_error)



plt.figure(dpi=300) # Used with the saving to improve the quality of the saved image

# the yerr input is the standard error on y
# the fmt input sets the format '.' for points, 'x' for crosses, '-' for a line. Letter is colour
#a = plt.plot(max_V_times, Vs, 'k.', linewidth=2.5)    # So this is y against x with y error bars from 'y_err' data, with black dots.
a = plt.errorbar(inverse_V, max_V_times1, yerr=times_error1,fmt='b.', lw=1.2, capsize=3, capthick=1.0)
plt.errorbar(inverse_V, max_V_times2, yerr=times_error2,fmt='r.', lw=1.2, capsize=3, capthick=1.0)

plt.savefig('Report/Graph.png') # Save the graph for a higher quality image

fit_par,cov = np.polyfit(inverse_V, max_V_times, 1, cov=True)

gradient = fit_par[0]
intercept = fit_par[1]

# The first is the square of the standard error of the gradient
# The second is the square of the standard error of the intercept
# We use np.diag to get just these terms, we then square root them
fit_SE = np.sqrt(np.diag(cov))
gradient_SE = fit_SE[0]
intercept_SE = fit_SE[1]

print(f"\nGradient is {gradient:.5f} ± {gradient_SE:.5f}")
print(f"Intercept is {intercept:.5f} ± {intercept_SE:.5f}")
x_range_lower = 95
x_range_higher = 260       # Set x range limits here to adjust the plot with them and for the best fit line stuff below.

# The linspace function is giving us 20 points, linearly spaced from the range of points on the x-axis.
x_points = np.linspace(x_range_lower,x_range_higher,20)
# Using the gradient and intercept to calculate the y value for the line of best fit from the x values.
y_points = gradient*x_points+intercept

plt.plot(x_points, y_points, 'k-', linewidth=2.0)

#plt.plot(x2, y2, 'b-', linewidth=2.5, label='C2')
#plt.plot(x3, y3, 'g-', linewidth=2.5, label='C3')
#plt.plot(x4, y4, 'r-', linewidth=2.5, label='C4')
#plt.legend()

plt.ylabel("t / μs")
plt.xlabel("1/V / 10⁻³ V⁻¹")



#plt.show()
#plt.gca().set_aspect(0.00075)

#plt.savefig('Report/Graph.png') # Save the graph for a higher quality image

#x_range_lower = -0.05
#x_range_higher = 1.25       # Set x range limits here to adjust the plot with them and for the best fit line stuff below.
