import numpy as np
import cv2

cap = cv2.VideoCapture(
    "assets/video.mp4"
)  # Put 0 in place of video directory, for webcam

# Play Untill keypress
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    # Opening a canvas and display video/webcam on that
    image = np.zeros(frame.shape, np.uint8)  # it makes entire numpy array 0s ie blank
    #                      ^
    #           pasting shape of frame

    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    image[: height // 2, : width // 2] = smaller_frame
    image[height // 2 :, : width // 2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[: height // 2, width // 2 :] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height // 2 :, width // 2 :] = smaller_frame
    cv2.imshow("frame", image)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
