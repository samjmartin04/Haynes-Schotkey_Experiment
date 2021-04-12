import matplotlib.pyplot as plt
import random

x_points = [0]
y_points = [0]
lim_lower = -50
lim_upper = 50

plt.plot(x_points, y_points, 'k-')

plt.xlim(lim_lower, lim_upper)        # x range of data
plt.ylim(lim_lower, lim_upper)

plt.show()

n = 0
while n < 100:
    prev_x = x_points[len(x_points)-1]
    delta_x = random.random()
    if random.random() < 0.5:
        delta_x *= -1
    new_x = prev_x + delta_x
    if new_x < lim_lower:
        new_x = lim_lower
    elif new_x > lim_upper:
        new_x = lim_upper
    x_points.append(new_x)

    prev_y = y_points[len(y_points)-1]
    delta_y = random.random()
    if random.random() < 0.5:
        delta_y *= -1
    new_y = prev_y + delta_y
    if new_y < lim_lower:
        new_y = lim_lower
    elif new_y > lim_upper:
        new_y = lim_upper
    y_points.append(new_y)


    n += 1
