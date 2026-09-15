from pathlib import Path

import cv2


# read video
PROJECT_ROOT = Path(__file__).resolve().parents[1]
video_path = PROJECT_ROOT / 'assets' / 'videos' / 'rocket.mp4'

video = cv2.VideoCapture(video_path)

# visualize video

ret = True
while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40)

video.release()
cv2.destroyAllWindows()
