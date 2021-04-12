import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import random
import numpy as np
import math


def func(x, a, b, c):
    return a*x**2 + b*x + c

def exp_func1(t, a, b, c, d):
    return a*np.exp(-(b-c*t)**2/4*d*t)

def exp_func(x, a, b, c):
    return a*np.exp(-(x-b)**2/c)

def exp_fun(x, a, b, c, d):
    return (a/c*math.sqrt(2*math.pi))*np.exp(-(x-b)**2/2*c**2) + d

def exp_func2(x, a, b, c, d):
    global max_y
    return a*np.exp(-(x-b)**2/2*c**2)


column1, column2, column3 = np.loadtxt('data/A C1.csv', delimiter=',', unpack=True)

crop_amount1 = 400
crop_amount2 = 850
x_data = column1[crop_amount1:crop_amount2]
y_data = column3[crop_amount1:crop_amount2]

max_y = 0
n = 0
while n < len(y_data):
    if y_data[n] > max_y:
        max_y = y_data[n]
    n += 1
print(max_y)

a = plt.plot(x_data, y_data, 'k.')
#plt.show()

popt, pcov = curve_fit(exp_func2, x_data, y_data, maxfev=1000000)
print(popt)

x_fit = np.linspace(0.000002, 0.0000045, 50)
#y_fit = exp_func(x_fit, popt[0], popt[1], popt[2])
#y_fit = exp_func2(x_fit, 5000, 0.000003, 105)
#y_fit += 1
y_fit = exp_func2(x_fit, popt[0], popt[1], popt[2], popt[3])
max_y_fit = popt[2]*math.sqrt(2*math.pi)
y_fit *= max_y_fit
#y_fit = exp_func2(x_fit, -1.76e3, 4.31e-1, 2.49, 1e3)

plt.plot(x_fit, y_fit, 'b-')
plt.show()
