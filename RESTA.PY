
import cv2
import numpy as np

#Se leen las imagenes
img1 = cv2.imread('IMG1.jpg',0)
img2 = cv2.imread('IMG2.jpg',0)

img1a=np.float_(img1)
img2a=np.float_(img2)
RST= ((img1a - img2a)+200) 
rst= RST.astype(np.uint8)

#Visualizamos los resultados
cv2.imshow('RESTA',rst)

cv2.waitKey(0)
cv2.destroyAllWindows()
