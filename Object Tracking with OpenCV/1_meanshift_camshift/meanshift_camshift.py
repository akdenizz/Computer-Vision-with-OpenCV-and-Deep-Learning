# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:20:08 2021

@author: asus
"""




import cv2
import numpy as np

# open camera
cap = cv2.VideoCapture(0)

# read one frame
ret, frame = cap.read()

if ret == False:
    print("Warning!")
    
# detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")    
face_rects = face_cascade.detectMultiScale(frame)

(face_x, face_y, w, h) = tuple(face_rects[0])
track_window = (face_x, face_y, w, h) # meanshift algorithm input

# region of interest
roi = frame[face_y:face_y + h, face_x : face_x + w] # roi = face

hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

roi_hist = cv2.calcHist([hsv_roi],[0],None,[180],[0,180]) # histogram required for tracking
cv2.normalize(roi_hist , roi_hist ,0 ,255, cv2.NORM_MINMAX)

#stopping criteria for tracking algorithm
# count = maximum number of items to be calculated
# eps = change
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 5, 1)

while True:
    
    ret, frame = cap.read()
    
    if ret:
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # we use the histogram to find in an image
        # pixel comparison
        
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180],1)

        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        
        x,y,w,h = track_window
        
        img2 = cv2.rectangle(frame, (x,y), (x+w, y+h),(0,0,255),5)
        
        cv2.imshow("Track", img2)
        
        if cv2.waitKey(1) & 0xFF == ord("q"): break
            
cap.release()
cv2.destroyAllWindows()
        


























