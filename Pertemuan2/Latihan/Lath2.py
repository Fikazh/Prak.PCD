import numpy as np
import cv2 as cv

imgRGB = cv.imread("../upn.jpg", cv.IMREAD_COLOR)
imgGrayscale = cv.imread("../upn.jpg", cv.IMREAD_GRAYSCALE)

pxRgb = imgRGB[100, 100]
blue = imgRGB[100, 100, 0]
imgRGB[100, 100] = [255, 255, 255]
pxGrayscale = imgGrayscale[100, 100]
imgGrayscale[100, 100] = 255

print(pxRgb)
print(blue)
print(imgRGB[100, 100])
print(pxGrayscale)
print(imgGrayscale[100, 100])

# b, g, r = cv.split(imgRGB)
# imgRGBMerge = cv.merge((b, g, r))
b = imgRGB[:, :, 0]
imgRGB[:, :, 2] = 0

cv.namedWindow("Image imgRGB Layer Blue", cv.WINDOW_NORMAL)
cv.imshow("Image imgRGB Layer Blue", b)
cv.namedWindow("Image imgRGB dengan Layer Red = 0", cv.WINDOW_NORMAL)
cv.imshow("Image imgRGB dengan Layer Red = 0", imgRGB)
cv.waitKey(0)
cv.destroyAllWindows()
