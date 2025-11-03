import numpy as np
import cv2

cap = cv2.VideoCapture("assets/video.mp4")

while True:

    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # How to Draw a line
    img = cv2.line(
        frame, (0, 0), (width, height), (255, 0, 0), 10
    )  # It will draw line from top left to shape of frame

    # syntax is: cv2.line(frame, (Starting coordinates), (Ending Coordinates), (RGB of color of line), Thickness of line in px)

    # Coordinates in OpenCV starts from 0,0 which is top left corner of frame

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
