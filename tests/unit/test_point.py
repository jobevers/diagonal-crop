import math

from diagonal_crop import point

from tests.unit import base


class PointTest(base.TestCase):
    def testAdd(self):
        self.assertPointEqual(
            point.Point(2, 3), point.Point(1, 1) + point.Point(1, 2))

    def testSubtract(self):
        self.assertPointEqual(
            point.Point(1, 0), point.Point(2, 1) - point.Point(1, 1))

    def testRecenter(self):
        p = point.Point(1, 1)
        old_center = point.Point(0, 0)
        new_center = point.Point(1, 1)
        result = point.Point(2, 2)
        self.assertPointEqual(result, p.recenter(old_center, new_center))

    def testRotate90Degrees(self):
        p = point.Point(1, 0)
        center = point.Point(0, 0)
        result = point.Point(0, 1)
        self.assertPointEqual(result, p.rotate(center, math.pi / 2))
