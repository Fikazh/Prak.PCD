import numpy as np
import cv2 as cv

soekarnoIMG = cv.imread("../soekarno.jpg")
hattaIMG = cv.imread("../hatta.jpg")

rows, cols, channels = hattaIMG.shape
roi = soekarnoIMG[0:rows, 0:cols]

roiadd = cv.add(roi, 50)
roisub = cv.subtract(roi, 50)
hattaIMGadd = cv.add(hattaIMG, 50)
hattaIMGsub = cv.subtract(hattaIMG, 50)

cv.imshow("ROI Add", roiadd)
cv.imshow("ROI Subtract", roisub)
cv.imshow("hatta Add", hattaIMGadd)
cv.imshow("hatta Subtract", hattaIMGsub)

cv.waitKey(0)
cv.destroyAllWindows()
