import numpy as np
import cv2 as cv

imgRGB = cv.imread("../upn.jpg")

tiang = imgRGB[25:280, 230:290]
imgRGB[25:280, 20:80] = tiang

cv.imshow("Gambar", imgRGB)

cv.waitKey(0)
cv.destroyAllWindows
