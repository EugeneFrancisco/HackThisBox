import cv2
from PIL import Image
import numpy as np

#======================== IMAGE ==================

image = cv2.imread("/content/July5LivePlant3A.jpg", 1)

#======================== CROPPING IMAGE =========================================

#croppedImage = image[:768,200:450]
#cv2_imshow(croppedImage)
#cv2.imwrite("/content/photos/image0300bw.jpg", image)

#======================= COLOR FORMATTING ===========================================

# Converts image to hsv format
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Defining the boundaries for green within the HSV format
lowerGreen = np.array([40, 50, 50])#40,50,50#lower bound for green
upperGreen = np.array([80, 255, 255])#80,255,255.     this is the upper bound for the green

#Mask is created using the lower and upper green bounds
mask = cv2.inRange(hsv, lowerGreen, upperGreen)# mask created which should only show colors in the lower and upper green range

# Cleaning artifacts from the image
kernel = np.ones((5,5),np.uint8)#Defining the size of a kernel
openedMask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)#Removes dots that are the size of the kernel
closedMask = cv2.morphologyEx(openedMask, cv2.MORPH_CLOSE, kernel)#Closes holes that are the size of the kernel

#===================== COUNTING GREEN PIXELS =================================

#Because the mask isolates the green channel, any white in the mask is green in the image.
#To count number of green pixels, the number of white pixels in the mask is counted instead

numWhitePix = np.sum(mask == 255)#Takes the mask and finds where the mask is white
print("NUM GREEN PIXLS====================", numWhitePix)

#===================== CREATING THE RESULT ===============================

cleanResult = cv2.bitwise_and(image, image, mask = closedMask)
#dirtyResult = cv2.bitwise_and(image, image, mask = mask)
#gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
#(_, binary) = cv2.threshold(gray, 1,255, cv2.THRESH_BINARY) #Pure black and white image. Effectively the mask


# ================ SHOWING THE IMAGES =====================
#cv2.imshow(image)
#cv2.imshow(mask)
#cv2.imshow(dirtyResult)
cv2.imshow(cleanResult)
#cv2.imshow(dirtyResult)
