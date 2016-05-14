#pylint: disable=invalid-name
import collections
import math


_Point = collections.namedtuple('Point', ['x', 'y'])


class Point(_Point):
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def recenter(self, old_center, new_center):
        return self + (new_center - old_center)

    # http://homepages.inf.ed.ac.uk/rbf/HIPR2/rotate.htm
    def rotate(self, center, angle):
        # angle should be in radians
        x = math.cos(angle) * (self.x - center.x) - math.sin(angle) * (self.y - center.y) + center.x
        y = math.sin(angle) * (self.x - center.x) + math.cos(angle) * (self.y - center.y) + center.y
        return Point(x, y)

