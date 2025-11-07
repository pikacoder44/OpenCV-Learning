import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()



    cv2.imshow("Frame", cap)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.releasekey()
cv2.destroyAllWindows()
