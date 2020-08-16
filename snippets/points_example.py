import math
from z3 import *
import numpy as np
import matplotlib.pyplot as plt

set_option(precision = 20)
plt.style.use('seaborn-whitegrid')

"""
Convert from Z3 to python float values. 
"""
def num (r) : 
    return float(r.numerator_as_long())/float(r.denominator_as_long())

"""
Convert from Z3 to python values. 
"""
def get_value (r) : 
    if is_int_value(r) : 
        return int(r)
    elif is_rational_value(r) :
        return num(r)
    elif is_algebraic_value(r) : 
        return num(r.approx(10))
    elif r is None : 
        None
    else :
        return num(r)
    
"""
Plot points onto a grid plane ==> Matplot grid.
"""
def plot_points (scatter_x, scatter_y, label="Default") : 
    
        plt.title(label)
        plt.ylim(-50, 250)
        plt.xlim(-50, 250)
        plt.axes().set_aspect('equal')
        colors = ["r", "b", "k", "m", "c", "y", "g", "w"] 
        nums = [x for x in range(len(scatter_x))]
        for (x, y, c, index) in zip(scatter_x, scatter_y, colors, nums) :
            _xr = round(x, 2)
            _yr = round(y, 2)
            plt.scatter([_xr], [_yr], color=c)
            plt.annotate(f"P{index} ({_xr}, {_yr})", (x, y), horizontalalignment='left', verticalalignment='bottom')
        
        plt.show()
        
"""
Need a clockwise ordering of points using sorting technique
=> Works by comparing radian angle subtended from shape centriod.
"""
def sort_points (plot_x, plot_y) : 
    print("Sorting Points")
    points = []
    for (x, y) in zip (plot_x, plot_y) : 
        points.append((x, y))
    # Suggest ==>  Take about a corner point, check for clockwise cycle.
    center_point = (sum([p[0] for p in points]) / len(points), sum([p[1] for p in points]) / len(points))
    # center_point = points[0]
    # Checking w.r.t Origin of coordinate system ==> Didn't work.
    # center_point = points[0]
    points.sort(key = lambda point : math.atan2(point[1] - center_point[1], point[0] - center_point[0]))
    (A, B) = ([], [])
    for (x, y) in points : 
        A.append(x)
        B.append(y)

    return (A, B)
