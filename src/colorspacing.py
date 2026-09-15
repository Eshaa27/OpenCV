from pathlib import Path

import cv2


PROJECT_ROOT = Path(__file__).resolve().parents[1]
img = cv2.imread(str(PROJECT_ROOT / 'outputs' / 'udaan_out.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('img', img)
cv2.imshow('img_rgb', img_rgb)
cv2.waitKey(0)
