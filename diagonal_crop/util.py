from __future__ import division

import collections
import math

from diagonal_crop import point


def getCenter(im):
    return point.Point(*(d / 2 for d in im.size))


Bound = collections.namedtuple('Bound', ('left', 'upper', 'right', 'lower'))


def getBounds(points):
    x, y = zip(*points)
    # left, upper, right, lower using the usual image coordinate system
    # where top-left of the image is 0, 0
    return Bound(min(x), min(y), max(x), max(y))


def getBoundsCenter(bounds):
    return point.Point(
        (bounds.right - bounds.left) / 2 + bounds.left,
        (bounds.lower - bounds.upper) / 2 + bounds.upper
    )


def roundint(value):
    return int(round(value))


def getRotatedRectanglePoints(angle, base_point, height, width):
    a = point.Point(
        width * math.cos(angle),
        -width * math.sin(angle)
    )
    c = point.Point(
        a.x + height * math.sin(angle),
        a.y + height * math.cos(angle)
    )
    b = point.Point(
        height * math.cos(math.pi / 2 - angle),
        height * math.sin(math.pi / 2 - angle)
    )
    return tuple(base_point + x for x in (point.Point(0, 0), a, c, b))
