import cv2

# Load Image in python
img = cv2.imread("assets/logo.png", 1)

# Display Image:
cv2.imshow("Image", img)


# Close
cv2.waitKey(0) # waits for 0 seconds
cv2.destroyAllWindows()
