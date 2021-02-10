# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 17:27:45 2021

@author: asus
"""

"""
Import OpenCv library

Import Numpy library

Import image as black and white and visualize it

Apply Edge Detection

Import the haar cascade required for face detection

Make face detection and visualize the results

Initialize the HOG , get the people detector and  set the SVM

Apply the people detection algorithm on image and visualize

"""


import cv2

import numpy as np

# Import image as black and white and visualize it
img = cv2.imread("example.jpg", 0)
cv2.imshow("Example", img)

#Apply Edge Detection
edges = cv2.Canny(image = img, threshold1 = 200, threshold2 = 255)
cv2.imshow('Edge Detection',edges)

#Import the haar cascade required for face detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Make face detection and visualize the results
face_rect = face_cascade.detectMultiScale(img)
for (x,y,w,h) in face_rect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),10)
cv2.imshow("Face Detection", img)

#Initialize the HOG , get the people detector and  set the SVM
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#Apply the people detection algorithm on image and visualize
(rects, weights) = hog.detectMultiScale(img, padding=(8, 8), scale=1.05)

for (xA, yA, xB, yB) in rects:
    cv2.rectangle(img, (xA, yA), (xB, yB), (0, 0, 255), 2)
	
cv2.imshow("People Detection", img)



