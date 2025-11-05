import numpy as np
import cv2

img = cv2.imread("assets/chessboard.png")
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

# First we have to convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect Corners
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
# This returns numpy array of floating numbers so we have to convert it to int
corners = np.int64(corners)

for corner in corners:
    x, y = corner.ravel()  # it will do this: [[1,2] , [2,1]]  to [1,2,2,1]
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)


cv2.imshow("Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
