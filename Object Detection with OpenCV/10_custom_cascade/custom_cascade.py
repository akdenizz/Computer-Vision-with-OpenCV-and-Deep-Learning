# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 16:30:50 2021

@author: asus
"""

"""
1) data set:
    n,p(negative,positive)
2) download cascade program (https://amin-ahmadi.com/cascade-trainer-gui/)
3) generate cascade 
4) code the detection algorithm using cascade

    
"""

import cv2
import os 

# image storage folder
path = "images"  # ; after running these codes; change image0  as  n, image1 as p

# size of images
imgWidth = 180
imgHeight = 120

#video capture

cap = cv2.VideoCapture(0) # 0 bc of using default camera
# pixels of camera
cap.set(3, 640)
cap.set(4, 480)
cap.set(10,180) #brightness



global countFolder

def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists(path + str(countFolder)):
        countFolder += 1
    os.makedirs(path+str(countFolder))    
    
saveDataFunc()    

count = 0
countSave = 0

while True :
    success, img = cap.read()
    
    if success:
        img = cv2.resize(img, (imgWidth, imgHeight))
        
        if count % 5 == 0:
            cv2.imwrite(path+str(countFolder)+"/"+str(countSave)+"__"+".png", img)
            countSave += 1
            print(countSave)
        count += 1
        
        cv2.imshow("Image", img)
        
    if cv2.waitKey(1)   & 0xFF == ord("q"):break
     
cap.release() 
cv2.destroyAllWindows()    























