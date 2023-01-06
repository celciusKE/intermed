#import the following modules
import numpy as np
import imageio.v2
import scipy.ndimage
import cv2

#take image input and assign variable to it
img="profile.jpg"

#convert image to sketch
def grayscale(rgb):
    #2d array to convert image to sketch
    return np.dot(rgb[..., :3], [0.299,0.587,0.114]) 

def dodge(front, back):
    #if image is greater than 255 convert it to 255
    result= front+255/(255-back)
    result[result>255]=255
    result[result==255]=255

    #converting sny suitable existing column to categorical type using aspect function
    #uint is for 8-bit signed integer
    return result.astype('uint8')

S=imageio.v2.imread(img)
gray=grayscale(S)
i=255-gray

#convert into a blur image
blur=scipy.ndimage.filters.gaussian_filter(i,sigma=10) 

#calling the function
r=dodge (blur,gray)

cv2.imwrite('profile.png',r)