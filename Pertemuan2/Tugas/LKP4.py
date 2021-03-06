import numpy as np
import cv2 as cv

soekarnoIMG = cv.imread("../soekarno.jpg", cv.IMREAD_GRAYSCALE)
hattaIMG = cv.imread("../hatta2.jpg", cv.IMREAD_GRAYSCALE)

rows, cols = hattaIMG.shape
roi = soekarnoIMG[0:rows, 0:cols]

roiadd = cv.add()
hattaIMGsub = cv.subtract(hattaIMG, 50)

cv.imshow("Soekarno Grayscale", roi)
cv.imshow("hatta Grayscale", hattaIMG)
cv.imshow("Soekarno Add", roiadd)
cv.imshow("hatta Subtract", hattaIMGsub)

cv.waitKey(0)
cv.destroyAllWindows()
