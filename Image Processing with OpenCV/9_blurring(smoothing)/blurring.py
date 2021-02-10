# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:24:24 2020

@author: asus
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# blurring (reduces details, blocks noise)
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("Original"), plt.show()

"""
Avarage Blur Method
- made by wrapping an image with a normalized can filter
- Averages all pixels below the kernel area and replaces this average with the central element
"""
dst2 = cv2.blur(img, ksize = (3,5))
plt.figure(), plt.imshow(dst2), plt.axis("off"), plt.title("Avarage Blur"), plt.show()









"""
Gaussian Blur Method

- In this method, Gaussian core is used instead of box filter.
- It specifies the width and height of the core, which should be positive and unique.
-SigmaX and SigmaY, We must specify the standard deviation in the X and Y directions.

"""

gb = cv2.GaussianBlur(img, ksize = (3,5), sigmaX = 7)
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("Gaussian Blur"), plt.show()











"""
Median Blur Method

- Takes the median of all pixels below the core area and the central element is replaced by this median value 
- Highly effective against salt and pepper noise

"""

mb = cv2.medianBlur(img, ksize = 3)
plt.figure(), plt.imshow(mb), plt.axis("off"), plt.title("Median Blur"), plt.show()

# Make gaussian noise
def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    
    gauss = np.random.normal(mean, sigma, (row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    
    return noisy

# import and normalize
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("Original"), plt.show()


gaussianNoisyImage = gaussianNoise(img)
plt.figure(), plt.imshow(gaussianNoisyImage), plt.axis("off"), plt.title("Gaussian Noise"), plt.show()

# gaussian blur 

gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize = (3,5), sigmaX = 7)
plt.figure(), plt.imshow(gb2), plt.axis("off"), plt.title("with Gauss Blur"), plt.show()

# Make salt and pepper noise

def saltPepperNoise(image):
    
    row, col, ch = image.shape
    s_vs_p = 0.5
    
    amount = 0.004
    
    noisy = np.copy(image)
    
    #salt - white
    num_salt = np.ceil(amount * image.size * s_vs_p) #ceil-rounds a decimal number(1.2-->1.0)
    coords = [np.random.randint(0, i-1, int(num_salt)) for i in image.shape ] 
    noisy[coords] = 1
    
    #pepper - black
    num_pepper = np.ceil(amount * image.size * (1-s_vs_p))
    coords = [np.random.randint(0, i-1, int(num_pepper)) for i in image.shape ] 
    noisy[coords] = 0

    return noisy


spImage = saltPepperNoise(img)
plt.figure(), plt.imshow(spImage), plt.axis("off"), plt.title("Salt Pepper Noise"), plt.show()


mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize = 3)
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("with Median Blur"), plt.show()







