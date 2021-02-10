# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:52:13 2020

@author: asus
"""
import cv2 
import numpy as np

# Generate an image
img = np.zeros((512,512,3), np.uint8) # black img
print(img.shape)

cv2.imshow("Black", img)

#Line

#(image, starting point, end point, color, thickness )
cv2.line(img, (0,0), (512,512), (0,255,0), 3)# RGB = (255,0,0) --> red (0,255,0)-->green (0,0,255)--> blue but opencv--> BGR
cv2.imshow("Line",img)

# Rectangle

#(img, startpt, endpt, color)
cv2.rectangle(img,(0,0), (256,256), (255,0,0), cv2.FILLED)
cv2.imshow("Rectangle",img)

# Circle

#(img, center, radius, color)
cv2.circle(img, (300,300),45,(0,0,255),cv2.FILLED)
cv2.imshow("Circle",img)

# Text

#(img, startpt, font, thickness ,color)
cv2.putText(img, "Image", (350,350),cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Image",img)