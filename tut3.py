import numpy as np
import cv2

cap = cv2.VideoCapture("assets/video.mp4") # Put 0 in place of video directory, for webcam

# Play Untill keypress
while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
