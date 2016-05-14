# diagonal-crop
Diagonally crop an image using python and pillow

# Usage

![Alt Text](media/lenna-crop-area.png?raw=true "Title")

The black box is the area that we want to crop.  It is a 150x200 rectangle rotated 45 degrees.  The red dot is the base, at (200, 250).

```python
import math
from PIL import Image
import diagonal_crop

im = Image.open('media/lenna.png')
angle = math.pi / 4
cropped_im = diagonal_crop.crop(im, (200, 250), angle, 150, 200)
```

![Alt Text](media/output.png?raw=true "Title")

# Methodology

Making the crop is relatively simple; at a high level the image is
rotated and then cropped.

For large images rotation can be expensive
so first, the image is cropped down to the bounding box of the target
area. The bounding box is shown in white:

![Alt Text](media/lenna-bounding-box.png?raw=true "Title")

And here is the result:

![Alt Text](media/bounding-box.png?raw=true "Title")

The new crop area is calculated:

![Alt Text](media/bounding-box-crop-area.png?raw=true "Title")

The image is rotated:

![Alt Text](media/rotated.png?raw=true "Title")

And, the crop area recalculated:

![Alt Text](media/rotated-crop-area.png?raw=true "Title")

This can then be cropped, giving the final result:

![Alt Text](media/output.png?raw=true "Title")
