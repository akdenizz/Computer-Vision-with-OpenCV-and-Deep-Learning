"""

Import opencv library

Import matplotlib library

Import the image as black and white 

Visualization 

Look at the shape of img

Resize the image by 4/5 ratio  and show the img

Put a text such as "Dog" in original img  and show the img



Make the ones above the threshold 50 value of the original image, white; make the ones below the threshold 50 value black,
 
Use binary threshold method and show the img

Apply the Gaussian Blurry in original image and show the img

Apply the Laplacian Gradient in original image and show the img

Draw Histogram of the original image



"""

# import opencv library
import cv2
# import matplotlib library
import matplotlib.pyplot as plt

# import the image as black and white 
img = cv2.imread("example.jpg", 0)

# visualization 
cv2.imshow("Example-1",img)

# Look at the shape of img
print(img.shape)

# resize the image by 4/5 ratio  and show the img
imgResized = cv2.resize(img, (int(img.shape[1]*4/5),int(img.shape[0]*4/5)))
print(imgResized.shape)
cv2.imshow("Resized Img",imgResized)

# Put a text such as "Dog" in original img  and show the img
cv2.putText(img, "Dog", (350,120),cv2.FONT_ITALIC, 3, (0,0,0))
cv2.imshow("Text w Img", img)


# Let's make the ones above the threshold 50 value of the original image, white; make the ones below the threshold 50 value black,
 
# Use binary threshold method and show the img
_, thresh_img = cv2.threshold(img, thresh = 50, maxval = 255, type = cv2.THRESH_BINARY)
cv2.imshow("Tresholded Img",thresh_img)

# Apply the Gaussian Blurry in original image and show the img
gb = cv2.GaussianBlur(img, ksize = (3,5), sigmaX = 7)
cv2.imshow("Gaussian Blurring",gb)

# Apply the Laplacian Gradient in original image and show the img
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_64F )
cv2.imshow("Laplacian Gradient", laplacian)

# Draw Histogram of the original image
img_hist = cv2.calcHist([img],channels = [0], mask = None , histSize = [256], ranges = [0,256]) 
plt.figure(), plt.plot(img_hist)

















