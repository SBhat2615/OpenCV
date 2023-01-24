
import cv2



''' IMAGE CAPTURE

img = cv2.imread("Resources/Photos/cat_large.jpg")
cv2.imshow("cat", img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

'''




#''' VIDEO CAPTURE

video = cv2.VideoCapture("/Users/siddhartha/Desktop/yolo/markers.mkv")
while True:
    success, img = video.read()
    cv2.imshow("Playing Dog", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

#'''




''' RESCALE VIDEOS & IMAGES

# Change resolution of images, videos & live videos
def rescaleFrame(frame):
    scale = 0.75
    width = int(frame.shape[1] * scale)     # 1 - width of image(frame of a video)
    height = int(frame.shape[0] * scale)    # 0 - height
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation = cv2.INTER_AREA)    ## Resize to particular dimension

# Change resolution of live videos
def changeResolution(width, height):
    video.set(3, width)
    video.set(4, height)

video = cv2.VideoCapture("Resources/Videos/dog.mp4")

while True:
    success, frame = video.read()
    frameResized = rescaleFrame(frame)
    cv2.imshow("Original", frame)                   # Original
    cv2.imshow("Resized video", frameResized)       # Resized
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

'''