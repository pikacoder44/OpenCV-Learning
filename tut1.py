import cv2

# Load Image in python
img = cv2.imread("assets/logo.png", 1)


# Resize image
# img = cv2.resize(img, (400, 400))
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)


# Rotate Image:
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Make a new image out of the manipulated one
cv2.imwrite("new_img.jpg", img)

# Display Image:
cv2.imshow("Image", img)


# Close
cv2.waitKey(0)  # waits for 0 seconds
cv2.destroyAllWindows()
