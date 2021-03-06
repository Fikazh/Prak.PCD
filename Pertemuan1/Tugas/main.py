import cv2 as cv

img = cv.imread("PangeranDiponogoro.jpg", cv.IMREAD_GRAYSCALE)

cv.namedWindow(
    "Pangeran Diponegoro - 11 November 1785 - Yogyakarta", cv.WINDOW_NORMAL)
cv.imshow("Pangeran Diponegoro - 11 November 1785 - Yogyakarta", img)

cv.imwrite("PangeranDiponogoroGrayscale.jpg", img)

cv.waitKey(0)
cv.destroyAllWindows()
