import matplotlib.pyplot as plt
import random
import pandas as pd
from matplotlib import rcParams
rcParams['lines.markersize'] = 8       # Data point size

finish_x = []

#Low Temp: -2 starting point. -0.8 and 0.75
#High Temp: -1 starting point. -1.0 and 1.2
#Normal: 0 starting point. -1.0 and 1.0

def random_walk(length_of_walk):       #Function takes number for the length of the walk.
    x_points = [0]      #array of the positions. Walk always starts at x = 0.

    n = 0
    decay = False
    while n < length_of_walk:       #Code runs for the number of iterations of the walk.
        prev_x = x_points[len(x_points)-1]  #prev_x is the particles starting point.
        delta_x = random.random()       #delta_x is the amount by which the particle moves.
        #delta_x = 1
        if random.random() < 0.01:
            #pass
            decay = True
            break       #10% chance of decaying so random walk stops there.
        if random.random() < 0.5:       #50% of the time, the particle moves to the left, where -ve x is left.
            delta_x *= -1
        else:
            delta_x *= 1
        new_x = prev_x + delta_x        #new_x is the particles new positions after the previous position has been changed by delta_x.
        #if new_x < lim_lower:       #If this new position is less than lim_lower (say outside of a box), it places it at this point.
        #    new_x = lim_lower
        #elif new_x > lim_upper:     #If this new position is greater than lim_upper (say outside of a box), it places it at this point.
        #    new_x = lim_upper
        x_points.append(new_x)
        n += 1
    return x_points[len(x_points)-1], decay    #Returns the finishing position of the particle.

lim_lower = -10         #Limits for how far the particle can go, as if constrained by say, a box.
lim_upper = 10

m = 0
while m < 100000:        #Number of random walks.
    new_x, decay = random_walk(15)  #new_x walk is the finishing position of the random walk.
    if not decay:
        finish_x.append(new_x)  #finish_x is the list of the finishing points from all of the random walks.
    m += 1

#print(finish_x)


n = 0
while n < len(finish_x):
    #finish_x[n] = round(finish_x[n], 0)     #All the finishing points are rounded to the nearest whole number to aid with plotting.
    finish_x[n] = round(finish_x[n], 1)
    n += 1
#print(finish_x)

x_dist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x_dist = []
n = 0
while n < 201:
    x_dist.append(0)
    n += 1
#x_dist is to represent the frequency of each of the finishing points from x = -10 to x = +10 with increments of 1.
#x_dist[0] corresponds to x = -10, x_dist[1] corresponds to x = -9, etc.


for x in finish_x:
    #index = int(x + 10)         #If x = -10, then it will add 1 to the x_dist[0]
    index = int(x*10 + 100)
    x_dist[index] += 1          #Does this for every single finishing point.
print(x_dist)

#x_dist_points = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
x_dist_points = []
n = 0
while n < 201:
    num = -10 + 0.1*n
    x_dist_points.append(num)
    n += 1

a = plt.plot(x_dist_points, x_dist, 'k.')       #Plot of frequency of the points (from x_dist) and their actual position in space (x_dist_points)

all_data = [[0, 0]]
n = 0
while n < len(x_dist_points):
    all_data.append([x_dist_points[n], x_dist[n]])
    n += 1

pd.DataFrame(all_data).to_csv("Data/Decay0.01.csv", header=None, index=None)
plt.xlim(lim_lower, lim_upper)
plt.show()
