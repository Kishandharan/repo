import cv2
import numpy as np
f14 = cv2.imread("F-14.png")
f14.resize(200,600)

cv2.imwrite("fighters.png",f14)
