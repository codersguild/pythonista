# https://startupnextdoor.com/computing-convex-hull-in-python/
# https://startupnextdoor.com/computing-convex-hull-in-python/

from collections import namedtuple  
import matplotlib.pyplot as plt  
import random
import math

Point = namedtuple('Point', 'x y')


class ConvexHull(object):  
    _points = []
    _hull_points = []

    def __init__(self):
        pass

    def add(self, point):
        self._points.append(point)

    def _get_orientation(self, origin, p1, p2):
        '''
        Returns the orientation of the Point p1 with regards to Point p2 using origin.
        Negative if p1 is clockwise of p2.
        :param p1:
        :param p2:
        :return: integer
        '''
        difference = (
            ((p2.x - origin.x) * (p1.y - origin.y))
            - ((p1.x - origin.x) * (p2.y - origin.y))
        )

        return difference

    def compute_hull(self):
        '''
        Computes the points that make up the convex hull.
        :return:
        '''
        points = self._points

        # get leftmost point
        start = points[0]
        min_x = start.x
        for p in points[1:]:
            if p.x < min_x:
                min_x = p.x
                start = p

        point = start
        self._hull_points.append(start)

        far_point = None
        while far_point is not start:

            # get the first point (initial max) to use to compare with others
            p1 = None
            for p in points:
                if p is point:
                    continue
                else:
                    p1 = p
                    break

            far_point = p1

            for p2 in points:
                # ensure we aren't comparing to self or pivot point
                if p2 is point or p2 is p1:
                    continue
                else:
                    direction = self._get_orientation(point, far_point, p2)
                    if direction > 0:
                        far_point = p2

            self._hull_points.append(far_point)
            point = far_point

    def get_hull_points(self):
        if self._points and not self._hull_points:
            self.compute_hull()

        return self._hull_points

    def display(self):
        # all points
        plt.ylim(-50, 250)
        plt.xlim(-50, 250)
        x = [p.x for p in self._points]
        y = [p.y for p in self._points]
        plt.plot(x, y, marker='.', linestyle='None')
        plt.axes().set_aspect('equal')
        # hull points
        hx = [p.x for p in self._hull_points]
        hy = [p.y for p in self._hull_points]
        plt.plot(hx, hy)
        plt.axes().set_aspect('equal')
        plt.title('Tangram Piece Hull')
        plt.show()

def sort_points (plot_x, plot_y) : 
    points = []
    for (x, y) in zip (plot_x, plot_y) : 
        points.append((x, y))
    
    center_point = (sum([p[0] for p in points]) / len(points), sum([p[1] for p in points]) / len(points))
    points.sort(key = lambda point : math.atan2(point[1] - center_point[1], point[0] - center_point[0]))
    (__plot_x, __plot_y) = ([], [])

    for (x, y) in points : 
        __plot_x.append(x)
        __plot_y.append(y)
        
    print((__plot_x, __plot_y))
    return (__plot_x, __plot_y)

def main():  
    ch = ConvexHull()
    # (X, Y) = ([10.5, 31.713203435596423, -10.713203435596427, -31.926406871192853], [37.0, 79.42640687119285, 100.63961030678928, 58.21320343559643])
    # (X, Y) = ([61.926406871192846, 19.5, 83.13961030678928, 40.71320343559643] [2.786796564403574, 24.0, 45.21320343559643, 66.42640687119285])
    # (X, Y) = [19.75, 62.176406871192846, -1.463203435596426, 40.96320343559643] [25.0, 46.21320343559643, 67.42640687119285, 88.63961030678928]
    # (X, Y) = ([10.75, -10.463203435596427, 31.963203435596423, 53.176406871192846], [38.0, 80.42640687119285, 101.63961030678928, 59.21320343559643])
    # (X, Y) = ([12.0, 116.43423229832085, 103.37995326103075, -1.0542790372901083], [32.0, 45.054279037290115, 149.48851133561098, 136.43423229832086])
    (X, Y) = ([0, 100, 100, 0],[0, 100, 0, 100])
    
    (plot_x, plot_y) = (X, Y)
    for (x, y) in zip (plot_x, plot_y) :
        ch.add(Point(x, y))

    print("Points on hull:", ch.get_hull_points())
    ch.display()


if __name__ == '__main__':  
    main()
