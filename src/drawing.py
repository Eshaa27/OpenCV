from pathlib import Path

import cv2


PROJECT_ROOT = Path(__file__).resolve().parents[1]
img = cv2.imread(str(PROJECT_ROOT / 'assets' / 'images' / 'udaan.jpg'))

print(img.shape)

# line
# cv2.line(img, (100, 900), (300, 450), (255, 255, 255), 3)

# # rectangle
# cv2.rectangle(img, (500, 50), (450, 600), (0, 0, 0), -1)
# # circle
# cv2.circle(img, (800, 200), 75, (255, 0, 0), 10)

# # text
cv2.putText(img, 'Hey you!', (600, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 10)

cv2.imshow('img', img)
cv2.waitKey(0)
