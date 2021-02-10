# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:24:24 2020

@author: asus
"""

import cv2
import numpy as np

#import the image

img = cv2.imread("lenna.png")
cv2.imshow("Original", img)

# Horizontal
hor = np.hstack((img,img))
cv2.imshow("Horizontal", hor)

# Vertical
ver = np.vstack((img,img))
cv2.imshow("Vertical", ver)
