import cv2
import numpy as np

# ''' Drawing shapes & putting texts

blankImage = np.zeros((500, 500, 3), dtype='uint8')
cv2.imshow("Blank image", blankImage)


# 1. Paint the image with certain color
'''
blankImage[:] = 0,255,0
cv2.imshow("Blank image with green paint", blankImage)


blankImage[200:300, 300:400] = 0,0,255
cv2.imshow("Blank image with a portion of red paint", blankImage)
'''


# 2. Draw a Rectangle
'''
#cv2.rectangle(blankImage, (0,0), (200,300), (0,255,0), thickness=2)
#cv2.imshow("Green border rectangle on a blank image", blankImage)


#cv2.rectangle(blankImage, (0,0), (200,300), (0,255,0), thickness=cv2.FILLED)    # thickness = -1
#cv2.imshow("Green filled rectangle on a blank image", blankImage)


cv2.rectangle(blankImage, (0,0), (blankImage.shape[1]//2, blankImage.shape[0]//2), (0,255,0), thickness=-1)
cv2.imshow("Green rectangle on a blank image", blankImage)
'''



# 3. Draw a Circle
'''
cv2.circle(blankImage, (blankImage.shape[1]//2, blankImage.shape[0]//2), 100, (0,0,255), thickness=3)
cv2.imshow("Circle with red border", blankImage)
'''



# 4. Draw a line
'''
cv2.line(blankImage, (0,0), (blankImage.shape[1]//2, blankImage.shape[0]//2), (255,255,255), thickness=3)
cv2.imshow("White line", blankImage)
'''


# 5. Write text on an Image
'''
cv2.putText(blankImage, "Guys, This is Wakanda !!!", (150,200), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)      # scale -> 1.0
cv2.imshow("Text on an Image", blankImage)
'''


cv2.waitKey(5000)
cv2.destroyAllWindows()
# '''