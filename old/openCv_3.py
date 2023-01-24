import cv2 as cv
import numpy as np

img = cv.imread("markers.png")

# Image blur & canny

imgBlur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
imgCanny = cv.Canny(imgBlur, 125, 175)   

# Number of contours

contours, hierarchies = cv.findContours(imgCanny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Drawing contours again on canny image (increase thickness) ; Increase clarity of contours

imgCanny = cv.drawContours(imgCanny, contours, -1, (255, 255, 255), 3)
contours, hierarchies = cv.findContours(imgCanny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.imshow("canny image", imgCanny)

# print(f"{len(contours)} contours found")

# Loop through the contours

for i in contours:

    # Area of contour
    area = cv.contourArea(i)

    # Ignore the contour area < 50
    if area<50:
        continue

    m = cv.moments(i)
    x, y = (m['m10'] / (m['m00'] + 1e-5), m['m01'] / (m['m00'] + 1e-5))

    if y>360:
        continue
    if y<100:
        continue
    # print(area)
    # print(x, y)

    img = cv.drawContours(img, [i], -1, (0,0,255), 1)

    x = int(x)
    y = int(y)
    o = 2
    color = img[x-o:x+o, y-o:y+o, :]
    color = np.mean(color, axis=(0, 1))
    # print(color)                            # Color in RGB format

    if ((209<color[0]<210) & (132<color[1]<133) & (29<color[2]<30)):
        print("Red-marker\n\n")
    
    elif ((172<color[0]<173) & (102<color[1]<103) & (25<color[2]<26)):
        print("Green-marker\n\n")

cv.imshow("result", img)


cv.waitKey(100000)
cv.destroyAllWindows()