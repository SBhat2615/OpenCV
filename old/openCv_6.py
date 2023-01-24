# COLOR SPACES

import cv2
import numpy as np

img = cv2.imread("Resources/Photos/cats.jpg")
cv2.imshow("Image", img)


'''
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", grayImg)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB", rgb)
'''


# REVERSE PROCESS POSSIBLE


b, g, r = cv2.split(img)

# Light color at specific place indicates higher concentration of that color
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Also can be merged to get back using merge function

cv2.waitKey(100000)
cv2.destroyAllWindows()