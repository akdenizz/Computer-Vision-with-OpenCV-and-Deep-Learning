# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:40:14 2020

@author: asus
"""

import cv2

img = cv2.imread("lenna.png") # if it will be ("lenna.png",0) , it shows black and white
print("Image Size:", img.shape)
cv2.imshow("Orjinal", img)

imgResized = cv2.resize(img, (800,800))
print("Resized Img Shape:", imgResized.shape)
cv2.imshow("Img Resized", imgResized)

# Crop
imgCropped = img[:200, :300] #normally it is width-height but in opencv --> heigth-width
cv2.imshow("Cropped Image", imgCropped)