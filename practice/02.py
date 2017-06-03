# Difference between io.imread() & cv2.imread()

from skimage import io, data
import cv2

img = io.imshow('fuck.jpg')
img1 = cv2.imread('fuck.jpg')

io.show()
