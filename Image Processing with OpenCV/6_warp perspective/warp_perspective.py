# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:38:09 2020

@author: asus
"""

import cv2
import numpy as np

# import the image
img = cv2.imread("card.png")
cv2.imshow("Original", img)

width = 400
height = 500

# You can check the points by opening the image with Paint 

pts1 = np.float32([[230,1], [1,472], [540,150], [338,617]])
pts2 = np.float32([[0,0], [0, height], [width,0], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
print (matrix)

imgOutput = cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("Final Image", imgOutput)







