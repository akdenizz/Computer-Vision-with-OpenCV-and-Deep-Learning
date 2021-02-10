# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:48:48 2020

@author: asus
"""

"""
Gradients
    - Image gradient is a directional change in density or color in the image
    - Used in edge detection

"""
import cv2
import matplotlib.pyplot as plt


#import img
img = cv2.imread("sudoku.jpg", 0)# 0 --> black and white
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Original Img")

# x gradient
sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 1, dy = 0, ksize = 5)
plt.figure(), plt.imshow(sobelx, cmap = "gray"), plt.axis("off"), plt.title("Sobel X")

# y gradient 
sobely = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 0, dy = 1, ksize = 5)
plt.figure(), plt.imshow(sobely, cmap = "gray"), plt.axis("off"), plt.title("Sobel Y")

#Laplacian Gradient
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_16S )
plt.figure(), plt.imshow(laplacian, cmap = "gray"), plt.axis("off"), plt.title("Laplacian")
