import numpy as np
import cv2 as cv

imgRGB = cv.imread("../upn.jpg", cv.IMREAD_COLOR)
imgGrayscale = cv.imread("../upn.jpg", cv.IMREAD_GRAYSCALE)

print("\nRGB Image")
print(imgRGB.shape)
print(imgRGB.size)
print(imgRGB.dtype)

print("\nGrayscale Image")
print(imgGrayscale.shape)
print(imgGrayscale.size)
print(imgGrayscale.dtype)
