# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:43:54 2020

@author: asus
"""

import cv2
import matplotlib.pyplot as plt

#import main image
chos = cv2.imread("chocolates.jpg", 0)
plt.figure(), plt.imshow(chos, cmap = "gray"), plt.axis("off")

#image to seach
cho = cv2.imread("nestle.jpg", 0)
plt.figure(), plt.imshow(cho, cmap = "gray"), plt.axis("off")

# orb identifier  --> object properties such as edge, vertice 
orb = cv2.ORB_create()

#key point detection
kp1, des1 = orb.detectAndCompute(cho, None)
kp2, des2 = orb.detectAndCompute(chos, None)

#brute force matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

#match the points
matches = bf.match(des1,des2)

#sort by distance
matches = sorted(matches, key = lambda  x: x.distance)

#visualize the matched images
plt.figure()
img_match = cv2.drawMatches(cho, kp1, chos, kp2, matches[:20], None, flags = 2)
plt.imshow(img_match), plt.axis("off"), plt.title("orb")

#sift(better than orb)
sift = cv2.xfeatures2d.SIFT_create()

#bf matches
bf = cv2.BFMatcher()

#key point detection with sift
kp1, des1 = sift.detectAndCompute(cho, None)
kp2, des2 = sift.detectAndCompute(chos, None)

matches = bf.knnMatch(des1, des2, k = 2)

nice_match = []

for match1, match2 in matches:
    if match1.distance < 0.75*match2.distance:
        nice_match.append([match1])

plt.figure()
sift_matches = cv2.drawMatchesKnn(cho, kp1, chos, kp2, nice_match, None, flags = 2)
plt.imshow(sift_matches), plt.axis("off"), plt.title("sift")












