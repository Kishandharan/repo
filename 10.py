import cv2
import numpy as np
image1="Dhoni.jpg"
src1=cv2.imread(image1)
for i in range(1,11,1):
    cv2.imwrite("Dhoni_"+str(i)+".jpg",src1)
image1="Dhoni.jpg"
image2="Dhoni.jpg"
image3="Dhoni.jpg"

src1 = cv2.imread(image1)
src2 = cv2.imread(image2)
src3 = cv2.imread(image3)

img3=np.concatenate((src1,src2,src3),axis=0)
cv2.imwrite('image1.png', img3)
img3=np.concatenate((src1,src2,src3),axis=1)
cv2.imwrite('image2.png', img3)
