# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 13:47:10 2020

@author: asus
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# import img
img = cv2.imread("contour.jpg", 0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off")

# for who has different version --> image, contours, hierarch = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
contours, hierarch = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)#img,parameter that says we want to find both inner and outer contours, allows us to compress horizontal, vertical, cross sections and leaves only endpoints 

external_contour = np.zeros(img.shape)
internal_contour = np.zeros(img.shape)

for i in range(len(contours)):
    
    #external
    if hierarch[0][i][3] == -1:
        cv2.drawContours(external_contour, contours, i, 255, -1)
    else: #internal
        cv2.drawContours(internal_contour, contours, i, 255, -1)

plt.figure(), plt.imshow(external_contour, cmap = "gray"), plt.axis("off")
plt.figure(), plt.imshow(internal_contour, cmap = "gray"), plt.axis("off")
