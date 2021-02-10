# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:10:07 2020

@author: asus
"""

"""
Morphological Operations

1- Erosion
    - The basic idea of erosion is just like soil erosion
    - It erodes the boundaries of the foreground object.
    
2- Dilation
    - It is opposite of the erode
    - Increases the white area in the image.

3- Opening
    - Opening = erode + dilation
    - It is useful in removing the noise.
    
4- Closing
    - Closing is opposite of opening
    - Dilation  +  Erode 
    - Useful for closing small holes in foreground objects or small black dots on objects
    
5- Morphological Gradient
    - It is the difference between the dilation and the erosion of a given image.
    
    
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

#import the img
img = cv2.imread("datai_team.jpg",0)

plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Original Img") 

# Erosion

kernel = np.ones((5,5), dtype=np.uint8)
result = cv2.erode(img, kernel, iterations = 1)

plt.figure(), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("Erosion Img") 


# Dilation

result2 = cv2.dilate(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("Dilation Img") 

# White Noise 
whiteNoise = np.random.randint(0,2, size = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("White Noise ") 

noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap = "gray"), plt.axis("off"), plt.title("White Noise w Img") 

# Opening
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("Opening") 


#Black Noise
blackNoise = np.random.randint(0,2, size = img.shape[:2])
blackNoise = blackNoise*-255
plt.figure(), plt.imshow(blackNoise, cmap = "gray"), plt.axis("off"), plt.title("Black Noise ") 

black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off"), plt.title("Black Noise w Img ") 


#Closing 

closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(closing, cmap = "gray"), plt.axis("off"), plt.title("Closing") 


# Morphological Gradient-edge detection

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap = "gray"), plt.axis("off"), plt.title("Gradient") 

















