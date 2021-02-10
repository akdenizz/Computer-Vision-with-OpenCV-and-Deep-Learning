# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:21:50 2020

@author: asus
"""

import cv2
import matplotlib.pyplot as plt


#import the images
einstein = cv2.imread("einstein.jpg", 0)
plt.figure(), plt.imshow(einstein, cmap = "gray"), plt.axis("off")

#classifier (classifies there is a face or not)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 

face_rect = face_cascade.detectMultiScale(einstein)

for (x,y,w,h) in face_rect:
    cv2.rectangle(einstein, (x,y), (x+w,y+h), (255,255,255),10)

plt.figure(), plt.imshow(einstein, cmap = "gray"), plt.axis("off")
    

#barcelona 
#import the img
barce = cv2.imread("barcelona.jpg", 0)
plt.figure(), plt.imshow(barce, cmap = "gray"), plt.axis("off")

face_rect = face_cascade.detectMultiScale(barce, minNeighbors = 7)

for (x,y,w,h) in face_rect:
    cv2.rectangle(barce, (x,y), (x+w,y+h), (255,255,255),10)

plt.figure(), plt.imshow(barce, cmap = "gray"), plt.axis("off")
    
#video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if ret:
        face_rect = face_cascade.detectMultiScale(frame, minNeighbors = 7)
        
        for (x,y,w,h) in face_rect:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255),10)
            cv2.imshow("face detect", frame)
            
        if cv2.waitKey(1) & 0xFF == ord("q") :break
        
cap.release()
cv2.destroyAllWindows()
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    