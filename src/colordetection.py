import cv2

from PIL import Image

from attch import get_limits

green=[0,255,255]
cap = cv2.VideoCapture(0)  # 0 is for the default camera
while True:
    ret,frame=cap.read()

    hsvimgcv2=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerlimit,upperlimit=get_limits(color=green)

    mask= cv2.inRange(hsvimgcv2, lowerlimit, upperlimit)

    mask_ = Image.fromarray(mask)

    bbox=mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1,y1), (x2, y2), (255, 0, 0),7)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xff== ord('t'):
        break

cap.release()

cv2.destroyAllWindows()
