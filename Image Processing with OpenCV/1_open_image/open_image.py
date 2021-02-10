# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 20:28:51 2020

@author: asus
"""

import cv2
 
# import the image
img = cv2.imread("messi5.jpg", 1) # 1 is color, 0 is gray
 
# visualization (show the img) 
cv2.imshow("ilk resim", img)

k = cv2.waitKeyEx(0) &0xFF

if k == 27: # wsc
    cv2.destroyAllWindows()
elif k == ord("q"):
    cv2.imwrite("messi_gray.png", img)
    cv2.destroyAllWindows()
    
    