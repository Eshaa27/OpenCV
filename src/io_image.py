from pathlib import Path

import cv2


# read image
PROJECT_ROOT = Path(__file__).resolve().parents[1]
image_path = PROJECT_ROOT / 'assets' / 'images' / 'marssurface.jpg'

img = cv2.imread(image_path)

# write image

cv2.imwrite(str(PROJECT_ROOT / 'outputs' / 'surface_out.jpg'), img)

# visualize image

cv2.imshow('image', img)
cv2.waitKey(5000)
