# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:36:34 2021

@author: asus
"""

"""
-It ignores smaller overlapping bounding boxes and returns only larger ones

-Calculates the Intersection over Union value between the boxes

-Boxes below a certain threshold value are eliminated

"""
import numpy as np
import cv2

def non_max_suppression(boxes, probs = None, overlapThresh=0.3):
    
    if len(boxes) == 0:
        return []
    
    if boxes.dtype.kind == "i":# if type is integer
        boxes = boxes.astype("float") # convert it as float
        
    x1 = boxes[:,0]
    y1 = boxes[:,1]
    x2 = boxes[:,2]
    y2 = boxes[:,3]
    
    # find the area
    area = (x2 - x1 + 1)*(y2 - y1 + 1)
    
    idxs = y2 # y coordinate in the lower left corner
    
    # value of probability
    if probs is not None:
        idxs = probs
        
    # sort index
    idxs = np.argsort(idxs)
    
    pick = [] # chosen boxes
    
    while len(idxs) > 0:
        
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)
        
        # max and min of x and y
        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])
        
        # find width and height
        w = np.maximum(0,xx2 - xx1 + 1)
        h = np.maximum(0,yy2 - yy1 + 1)
        
        # overlap-IoU 
        overlap = (w*h)/area[idxs[:last]]
        
        idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > overlapThresh)[0])))
        
    return boxes[pick].astype("int")
