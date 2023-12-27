import cv2
import numpy as np

img1 = cv2.imread("1.png")
img2 = cv2.imread("2.jpg")
img3 = cv2.imread("3.jpg")
final_image = numpy.vstack([img1, img2, img3])
cv2.imwrite("4.jpeg", final_image)
