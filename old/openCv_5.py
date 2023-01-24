import cv2
import numpy as np

img = cv2.imread("OPENCV/ma.png")
cv2.imshow("Image", img)


# Contour Detection

'''
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale Image", imgGray)

imgBlur = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)      # (3,3) -> kernel size of 2 by 2 tuple {ODD number}
cv2.imshow("Blur Image", imgBlur)

imgCanny = cv2.Canny(imgBlur, 125, 175)     # 125 & 175 -> Threshold values (google)
cv2.imshow("Canny edges", imgCanny)


ret, thresholdImage = cv2.threshold(imgGray, 125, 255, cv2.THRESH_BINARY)        # Binarize the image {below 125 to black(0) && below 255 to white}  &&  Convert image to binary
cv2.imshow("Threshold Image", thresholdImage)


contours, hierarchies = cv2.findContours(thresholdImage, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)        # pass thresholdImage or cannyImage
print(f"{len(contours)} contours found")
'''



# Draw contours on blank Image of canny edges(Of red colour)


imgCanny = cv2.Canny(img, 125, 175)
cv2.imshow("Canny edges", imgCanny)

contours, hierarchies = cv2.findContours(imgCanny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)        # 
print(f"{len(contours)} contours found")

blank = np.zeros(img.shape, dtype='uint8')
cv2.imshow("Blank Image", blank)

cv2.drawContours(blank, contours, -1, (0,0,255), 1)
cv2.imshow("Contours drawn", blank)




# Draw contours on blank Image of threshold image edges
'''
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale Image", imgGray)

ret, thresholdImage = cv2.threshold(imgGray, 125, 255, cv2.THRESH_BINARY)        # Binarize the image {below 125 to black(0) && below 255 to white}
cv2.imshow("Threshold Image", thresholdImage)


contours, hierarchies = cv2.findContours(thresholdImage, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)        # 
print(f"{len(contours)} contours found")

blank = np.zeros(img.shape, dtype='uint8')
cv2.imshow("Blank Image", blank)

cv2.drawContours(blank, contours, -1, (0,0,255), 1)
cv2.imshow("Contours drawn", blank)
'''



cv2.waitKey(100000)
cv2.destroyAllWindows()