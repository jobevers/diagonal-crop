from diagonal_crop.point import * # pylint: disable=wildcard-import
from diagonal_crop.util import * # pylint: disable=wildcard-import


def crop(im, base, angle, height, width):
    """Return a new, cropped image.

    Args:
        im: a PIL.Image instance
        base: a (x,y) tuple for the upper left point of the cropped area
        angle: angle, in radians, for which the cropped area should be rotated
        height: height in pixels of cropped area
        width: width in pixels of cropped area
    """
    base = Point(*base)
    points = getRotatedRectanglePoints(angle, base, height, width)
    return _cropWithPoints(im, angle, points)


def _cropWithPoints(im, angle, points):
    bounds = getBounds(points)
    im2 = im.crop(roundint(bounds))
    bound_center = getBoundsCenter(bounds)
    crop_center = getCenter(im2)
    # in the cropped image, this is where our points are
    crop_points = [pt.recenter(bound_center, crop_center) for pt in points]
    # this is where the rotated points would end up without expansion
    rotated_points = [pt.rotate(crop_center, angle) for pt in crop_points]
    # expand is necessary so that we don't lose any part of the picture
    im3 = im2.rotate(-angle * 180 / math.pi, expand=True)
    # but, since the image has been expanded, we need to recenter
    im3_center = getCenter(im3)
    rotated_expanded_points = [pt.recenter(crop_center, im3_center) for pt in rotated_points]
    im4 = im3.crop(roundint(getBounds(rotated_expanded_points)))
    return im4
