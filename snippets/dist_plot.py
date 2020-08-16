import math
import numpy as np
from functools import cmp_to_key
import matplotlib.pyplot as plt
from itertools import product

# (X, Y) = ([10.5, 31.713203435596423, -10.713203435596427, -31.926406871192853], [37.0, 79.42640687119285, 100.63961030678928, 58.21320343559643])
# (X, Y) = ([61.926406871192846, 19.5, 83.13961030678928, 40.71320343559643] [2.786796564403574, 24.0, 45.21320343559643, 66.42640687119285])
# (X, Y) = [19.75, 62.176406871192846, -1.463203435596426, 40.96320343559643] [25.0, 46.21320343559643, 67.42640687119285, 88.63961030678928]
# (X, Y) = ([10.75, -10.463203435596427, 31.963203435596423, 53.176406871192846], [38.0, 80.42640687119285, 101.63961030678928, 59.21320343559643])

(X, Y) = ([0, 100, 100, 0], [0, 100, 0, 50])
# (X, Y) = ([11.5, 32.71320343559643, -9.713203435596427, -30.926406871192853], [33.0, 75.42640687119285, 96.63961030678928, 54.21320343559643])

def sort_points (plot_x, plot_y) : 
    points = []
    for (x, y) in zip (plot_x, plot_y) : 
        points.append((x, y))
    
    center_point = (sum([p[0] for p in points]) / len(points), sum([p[1] for p in points]) / len(points))
    points.sort(key = lambda point : math.atan2(point[1] - center_point[1], point[0] - center_point[0]))
    (plot_x, plot_y) = ([], [])

    for (x, y) in points : 
        plot_x.append(x)
        plot_y.append(y)
        
    return (plot_x, plot_y)
    
def plot () : 
    plt.ylim(-50, 250)
    plt.xlim(-50, 250)
    (plot_x, plot_y) = sort_points(X, Y)
    plt.fill(plot_x, plot_y, "c")
    plt.axes().set_aspect('equal')
    plt.show()

plot()

# https://startupnextdoor.com/computing-convex-hull-in-python/