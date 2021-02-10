# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:07:58 2020

@author: asus
"""
import cv2
import matplotlib.pyplot as plt

# import img

img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # grayscale
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")
plt.show()

#thresholding
_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh_img, cmap = "gray")
plt.axis("off")
plt.show()




# adaptive thresholding
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)

plt.figure()
plt.imshow(thresh_img2, cmap = "gray")
plt.axis("off")
plt.show()






























