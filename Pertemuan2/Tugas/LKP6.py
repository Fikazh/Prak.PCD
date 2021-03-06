import numpy as np
import cv2 as cv

soekarnoIMG = cv.imread("../soekarno.jpg")
hattaIMG = cv.imread("../hatta2.jpg")

hattaIMGcut = hattaIMG[0:393, 390:700]
soekarnoIMG[0:393, 390:700] = hattaIMGcut

cv.namedWindow("soekarno", cv.WINDOW_NORMAL)
cv.imshow("soekarno", soekarnoIMG)

cv.waitKey(0)
cv.destroyAllWindows()
