# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 13:28:20 2020

@author: asus
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

#import img
img = cv2.imread("sudoku.jpg", 0)
img = np.float32(img)
print(img.shape)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off")

# Harris corner detection
dst = cv2.cornerHarris(img, blockSize = 2, ksize = 3, k = 0.04)
plt.figure(), plt.imshow(dst, cmap = "gray"), plt.axis("off")

dst = cv2.dilate(dst, None)
img[dst>0.2*dst.max()] = 1
plt.figure(), plt.imshow(dst, cmap = "gray"), plt.axis("off")

#shai tomasi detection
img = cv2.imread("sudoku.jpg", 0)
img = np.float32(img)
corners = cv2.goodFeaturesToTrack(img, 150, 0.01, 10) # img, edge number,quality level, min distance
corners = np.int64(corners)

for i in corners :
    x, y = i.ravel()
    cv2.circle(img, (x,y), 3, (125,125,125), cv2.FILLED)
    
plt.imshow(img)
plt.axis("off")  
    