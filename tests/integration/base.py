from PIL import ImageChops


# http://effbot.org/zone/pil-comparing-images.htm
def equal(im1, im2):
    """Returns True if two images are equal"""
    return ImageChops.difference(im1, im2).getbbox() is None
