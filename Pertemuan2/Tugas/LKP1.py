import numpy as np
import cv2 as cv

soekarnoGrayscale = cv.imread("../soekarno.jpg", cv.IMREAD_GRAYSCALE)
print("\nSoekarno Grayscale")
print(soekarnoGrayscale.shape)
print(soekarnoGrayscale.size)
print(soekarnoGrayscale.dtype)

hattaGrayscale = cv.imread("../hatta.jpg", cv.IMREAD_GRAYSCALE)

print("\nHatta Grayscale")
print(hattaGrayscale.shape)
print(hattaGrayscale.size)
print(hattaGrayscale.dtype)

soekarnoRGB = cv.imread("../soekarno.jpg", cv.IMREAD_COLOR)
print("\nSoekarno RGB")
print(soekarnoRGB.shape)
print(soekarnoRGB.size)
print(soekarnoRGB.dtype)

hattaRGB = cv.imread("../hatta.jpg", cv.IMREAD_COLOR)

print("\nHatta RGB")
print(hattaRGB.shape)
print(hattaRGB.size)
print(hattaRGB.dtype)
