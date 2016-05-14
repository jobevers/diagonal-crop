import math

import mock

from diagonal_crop import point
from diagonal_crop import util

from tests.unit import base


class UtilTest(base.TestCase):
    def testGetCenter(self):
        im = mock.Mock()
        im.size = (23, 82)
        self.assertPointEqual(point.Point(11.5, 41), util.getCenter(im))

    def testGetBounds(self):
        points = [point.Point(0, 0), point.Point(1, 0), point.Point(0, 1), point.Point(1, 1)]
        correct = util.Bound(0, 0, 1, 1)
        self.assertNamedTupleAlmostEqual(correct, util.getBounds(points))

    def testGetBoundsCenter(self):
        self.assertPointEqual(
            point.Point(.5, 1),
            util.getBoundsCenter(util.Bound(0, 0, 1, 2))
        )
        
    def testRoundint(self):
        self.assertEqual((5, 5), util.roundint((4.8, 5.1)))

    def testGetRotatedRectanglePoints(self):
        """Rotate a unit square by 45 degrees"""
        m = math.sqrt(2) / 2
        correct = (
            point.Point(0, 0),
            point.Point(m, -m),
            point.Point(2*m, 0),
            point.Point(m, m)
        )
        results = util.getRotatedRectanglePoints(math.pi / 4,  point.Point(0, 0), 1, 1)
        for points in zip(correct, results):
            self.assertPointEqual(*points)

