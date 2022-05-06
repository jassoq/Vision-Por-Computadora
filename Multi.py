#05/05/22
import cv2
import numpy as np

#Se leen las imagenes
img1 = cv2.imread('IMG1.jpg')
img2 = cv2.imread('IMG2.jpg')

img1a=np.float_(img1)
img2a=np.float_(img2)

multi=(img1a * img2a)/255
x= multi.astype(np.uint8)

#Visualizamos los resultados
cv2.imshow('MULTIPLICATION',x)

cv2.waitKey(0)
cv2.destroyAllWindows()