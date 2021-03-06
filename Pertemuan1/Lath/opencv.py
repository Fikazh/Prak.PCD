import numpy as np
import cv2 as cv

img_rgb = cv.imread("upn.jpg", cv.IMREAD_COLOR)
img_gray = cv.imread('upn.jpg', cv.IMREAD_GRAYSCALE)

cv.imwrite("upn_grayscale.jpg", img_gray)

cv.namedWindow('Image RGB', cv.WINDOW_NORMAL)
cv.imshow("Image RGB", img_rgb)

cv.namedWindow('Image Grayscale', cv.WINDOW_NORMAL)
cv.imshow('Image Grayscale', img_gray)

cv.waitKey(0)
cv.destroyAllWindows()
