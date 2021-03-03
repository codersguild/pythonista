import numpy as np
from itertools import product
import matplotlib.pyplot as plt


class Grid():

    def __init__(self, bound_x, bound_y):
        self.bound_x = bound_x
        self.bound_y = bound_y
        self.x_points = np.arange(0, bound_x, 10)
        self.y_points = np.arange(0, bound_y, 10)
        self.points = list(product(self.x_points, self.y_points))
        self.grid = dict()

    """
    Initiate the whole grid. Assign z3 variable to all points. 
    """

    def init_grid(self):
        for point in self.points:
            self.grid[point] = point

    """
    Show the intersection points of the grid
    """

    def show_grid_points(self):
        plt.ylim(0, self.bound_x)
        plt.xlim(0, self.bound_y)
        plt.style.use('seaborn-whitegrid')
        plt.figure(figsize=(20, 15))
        points = np.array(self.points)
        plt.plot(points[:, 0], points[:, 1], '.')
        plt.axes().set_aspect('equal')
        plt.show()
