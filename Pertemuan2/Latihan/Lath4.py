import numpy as np
import cv2 as cv

imgUpn = cv.imread("../upn.jpg")
imgUpnLogo = cv.imread("../Logo_UPNVJ.png")

# Meletakkan sebuah logo di sudut kiri atas, dan menyimpannya membuat ROI
rows, cols, channels = imgUpnLogo.shape
roi = imgUpn[0:rows, 0:cols]

# Buat sebuah mask dari logo dan mask inverse logo
img2gray = cv.cvtColor(imgUpnLogo, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

# Area black - out dari Logo dalam ROI
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

# Ambil hanya region dari logo dalam gambar logo
img2_fg = cv.bitwise_and(imgUpnLogo, imgUpnLogo, mask=mask)

# letakkan logo dalam ROI dan modifikasi citra utama
dst = cv.add(img1_bg, img2_fg)
imgUpn[0:rows, 0:cols] = dst

cv.imshow("Logo UPNVJ", imgUpn)

cv.waitKey(0)
cv.destroyAllWindows()
