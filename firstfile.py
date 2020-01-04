import cv2  #importing opencv
import numpy as np #importing numpy

img = cv2.imread('sampleimage.jpg',0) # for reading an image -> 0 to read in grey-scale
print(img)  #prints the intensity levels of each pixel in a row-wise list

img1 = cv2.imread('sampleimage.jpg',1) # 1 for reading a color image
print(img1) #prints each pixels bgr values row wise 

cv2.imshow('image',img1) #print image. First parameter is the name of the the window and second is name of the image 
cv2.waitKey(0) #cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. 
                #The function waits for specified milliseconds for any keyboard event.
                # If you press any key in that time, the program continues.
                # If 0 is passed, it waits indefinitely for a key stroke.
cv2.destroyAllWindows() #destroys all the windows





















import glob #??????????????????????????????

