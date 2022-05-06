#Librerias 
import numpy as np
import cv2 as cv

#Imagen cargada
imgCargar = "IMG.jpg"

#Proceso de la imagen 
imgColor = cv.imread(imgCargar,1)
imgColorB = cv.imread(imgCargar,1)
imgColorN = cv.imread(imgCargar,1)

cv.imshow('Original',imgColorB)

#PARAMETROS IMAGEN
h,w = imgColorB.shape[:2]


#VERTICAL
contw = w-1
#RECORRER LA MATRIZ

for i in range (0,h):
	for j in range (0,w):
		#Cambiamos la posicion
		imgColor [i][j] = imgColorN [i] [contw]
		contw = contw - 1
	contw = w-1
cv.imshow("Vertical",imgColor)

#HORIZONTAL

conth = h-1
#RECORRER LA MATRIZ

for i in range (0,h):
	for j in range (0,w):
		#Cambiamos la posicion
		imgColor [i][j] = imgColorN [conth] [j]
	conth = conth - 1
	
cv.imshow("Horizontal",imgColor)


cv.waitKey(0) 
cv.destroyAllWindows()
