import cv2 as cv
import numpy as np

# For video

video = cv.VideoCapture("allMarkers.mp4")

if video.isOpened() == False:
    print("Error while opening video")

while 1:
    _, img = video.read()
    
    imgBlur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
    imgCanny = cv.Canny(imgBlur, 125, 175)   

    # Number of contours
    contours, hierarchies = cv.findContours(imgCanny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    
    # Drawing contours again on canny image (increase thickness) ; Increase clarity of contours
    imgCanny = cv.drawContours(imgCanny, contours, -1, (255, 255, 255), 3)
    contours, hierarchies = cv.findContours(imgCanny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


    existing_objects = []
    obj_min_size = 5

    # Loop through the contours
    for i in contours:

        # Area of contour
        area = cv.contourArea(i)

        # Ignore the contour area < 50
        if area<50:
            continue
        m = cv.moments(i)
        x, y = (m['m10'] / (m['m00'] + 1e-5), m['m01'] / (m['m00'] + 1e-5))

        if y>650:
            continue
        if y<250:
            continue

        # Prevent duplication of values for objects
        skip = False
        for existing_pos in existing_objects:
            if existing_pos[0]>=x-obj_min_size and existing_pos[0]<=x+obj_min_size:
                if existing_pos[1]>=y-obj_min_size and existing_pos[1]<=y+obj_min_size:
                    skip = True
                    break
        if skip:
            continue
        
        existing_objects.append((x, y))

        # Draw contours on objects
        img = cv.drawContours(img, [i], -1, (0,0,255), 3)
        imgCanny = cv.drawContours(imgCanny, [i], -1, (255), 3)
    
        # Find out average BGR values of objects
        x = int(x)
        y = int(y)
        o = 2
        color = img[y-o:y+o, x-o:x+o,:]
        color = np.mean(color, axis=(0, 1))         # Color in BGR format

        
        # Colour matching 
        if((1<color[0]<4) and (-1<color[1]<3) and (72<color[2]<75)):
            print("mb_marker_buoy_red")
            
        elif ((23<color[0]<33) and (44<color[1]<54) and (5<color[2]<10)):
            print("mb_marker_buoy_green")
        
        elif ((-1<color[0]<1) and (-1<color[1]<1) and (-1<color[2]<1)):
            print("mb_marker_buoy_black")
        
        elif ((116<color[0]<126) and (116<color[1]<126) and (116<color[2]<126)):
            print("mb_marker_buoy_white")
        
        elif ((-1<color[0]<1) and (-1<color[1]<1) and (-1<color[2]<1)):
            print("mb_round_buoy_black")
        
        elif ((-1<color[0]<5) and (5<color[1]<30) and (90<color[2]<150)):
            print("mb_round_buoy_orange")
        
        
video.release()
cv.destroyAllWindows()