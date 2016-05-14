from __future__ import division

import collections
import math

from diagonal_crop import point


def getCenter(im):
    return point.Point(*(d / 2 for d in im.size))


Bound = collections.namedtuple('Bound', ('left', 'upper', 'right', 'lower'))


def getBounds(points):
    xs, ys = zip(*points)
    # left, upper, right, lower using the usual image coordinate system
    # where top-left of the image is 0, 0
    return Bound(min(xs), min(ys), max(xs), max(ys))


def getBoundsCenter(bounds):
    return point.Point(
        (bounds.right - bounds.left) / 2 + bounds.left,
        (bounds.lower - bounds.upper) / 2 + bounds.upper
    )


def roundint(values):
    return tuple(int(round(v)) for v in values)


def getRotatedRectanglePoints(angle, base_point, height, width):
    # base_point is the upper left (ul)
    ur = point.Point(
        width * math.cos(angle),
        -width * math.sin(angle)
    )
    lr = point.Point(
        ur.x + height * math.sin(angle),
        ur.y + height * math.cos(angle)
    )
    ll = point.Point(
        height * math.cos(math.pi / 2 - angle),
        height * math.sin(math.pi / 2 - angle)
    )
    return tuple(base_point + pt for pt in (point.Point(0, 0), ur, lr, ll))
