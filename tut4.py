import numpy as np
import cv2

cap = cv2.VideoCapture("assets/video.mp4")

while True:

    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # How to Draw a line
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)

    # How to Draw a ractangle
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5) # use -1 in thickness to fill ractangle

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
