import numpy as np
import cv2 as cv

soekarnoIMG = cv.imread("../soekarno.jpg")
hattaIMG = cv.imread("../hatta.jpg")

cv.imshow("soekarno image", soekarnoIMG)
cv.imshow("hatta image", hattaIMG)

rows, cols, channels = hattaIMG.shape
roi = soekarnoIMG[0:rows, 0:cols]

cv.imshow("roi", roi)

cv.waitKey(0)
cv.destroyAllWindows()
