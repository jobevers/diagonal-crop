import math
import os
import unittest

from PIL import Image
from PIL import ImageChops

import diagonal_crop


# http://effbot.org/zone/pil-comparing-images.htm
def equal(im1, im2):
    """Returns True if two images are equal"""
    return ImageChops.difference(im1, im2).getbbox() is None


class CropTest(unittest.TestCase):
    def testCrop(self):
        im = Image.open(os.path.join('media', 'lenna.png'))
        target = Image.open(os.path.join('media', 'output.png'))
        angle = math.pi / 4
        output = diagonal_crop.crop(im, (200, 250), angle, 150, 200)
        self.assertTrue(equal(target, output))
