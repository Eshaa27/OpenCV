import numpy as np
import cv2

def get_limits(color):
    # Convert BGR color to NumPy array
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)  # Convert to HSV

    # Define Green HSV Range
    lowerlimit = np.array([35, 100, 100], dtype=np.uint8)
    upperlimit = np.array([85, 255, 255], dtype=np.uint8)

    return lowerlimit, upperlimit

