# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 13:31:25 2021

@author: asus
"""



"""
- examnine data set (https://motchallenge.net/data/MOT17/)
- download data set ( you click Get all data in tle web site which is given above)
- convert img to video 
- eda(exploratory data analysis) -> gt(ground truth)
"""

import cv2
import os
from os.path import isfile, join
import matplotlib.pyplot as plt

pathIn = r"img1" # r = read and you can access this file(img1) in downloaded file
pathOut = "MOT17-13-SDP.mp4"

files = [f for f in os.listdir(pathIn) if isfile(join(pathIn,f))]

# img = cv2.imread(pathIn + "\\" + files[44]) --> read the img
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img) --> visualizing

fps = 25 # frame per second - it is written in website
size = (1920,1080)
out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*"MP4V"), fps, size, True)

for i in files:
    print(i)
    
    file_name = pathIn + "\\" + i
    
    img = cv2.imread(file_name)
    
    out.write(img)

out.release()




















