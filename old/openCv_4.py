
import cv2
import numpy as np

img = cv2.imread("Resources/Photos/cats.jpg")
cv2.imshow("Image", img)


# Translation
'''
def translate(img, x, y):
    translationMatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, translationMatrix, dimensions)

imgTranslated = translate(img, -100, 100)
cv2.imshow("Translate", imgTranslated)
'''



# Rotation
'''
def rotate(img, angle):
    rotationPoint = None
    (height, width) = img.shape[:2]
    if rotationPoint is None:
        rotationPoint = (width//2, height//2)
    
    rotationMatrix = cv2.getRotationMatrix2D(rotationPoint, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotationMatrix, dimensions)

rotated = rotate(img, -45)
cv2.imshow("Rotated Image", rotated)
'''



# Resize
'''

'''



# Flipping
'''
flip = cv2.flip(img, 0)             # 1 -> Horizontal flip, -1 -> Vertical + Horizonatal 
cv2.imshow("Flipped Image", flip)
'''



# Cropping
    # Prev video

cv2.waitKey(10000)
cv2.destroyAllWindows()