import cv2  #importing opencv
import numpy as np #importing numpy

img = cv2.imread('sampleimage.jpg',0) # for reading an image -> 0 to read in grey-scale
print(img)  #prints the intensity levels of each pixel in a row-wise list

img1 = cv2.imread('sampleimage.jpg',1) # 1 for reading a color image
print(img1) #prints each pixels bgr values row wise 

cv2.imshow('bgr_image',img1) #print image. First parameter is the name of the the window and second is name of the image 
cv2.waitKey(1000) #cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. 
                #The function waits for specified milliseconds for any keyboard event.
                # If you press any key in that time, the program continues.
                # If 0 is passed, it waits indefinitely for a key stroke.
cv2.destroyAllWindows() #destroys all the windows


b,g,r = cv2.split(img1)          #if the values are changed from bgr to rgb, the image would look like this
img2 = cv2.merge([r,g,b])
cv2.imshow('bgr_in_rgb_positions',img2)
cv2.waitKey(1000)


from matplotlib import pyplot as plt 


plt.imshow(img, cmap = 'Greys', interpolation = 'cubic')
#splt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show() #show image

















import glob #??????????????????????????????

