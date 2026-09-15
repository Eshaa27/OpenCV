from pathlib import Path

import cv2


PROJECT_ROOT = Path(__file__).resolve().parents[1]
img = cv2.imread(str(PROJECT_ROOT / 'assets' / 'images' / 'udaan.jpg'))

resized_img = cv2.resize(img, (640, 640))

print(img.shape)
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)
