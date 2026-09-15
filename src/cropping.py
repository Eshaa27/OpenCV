from pathlib import Path

import cv2


PROJECT_ROOT = Path(__file__).resolve().parents[1]
img = cv2.imread(str(PROJECT_ROOT / 'assets' / 'images' / 'udaan.jpg'))

print(img.shape)

cropped_img = img[220:740, 320:940]

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)
