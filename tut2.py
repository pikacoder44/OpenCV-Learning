import cv2

img = cv2.imread("assets/logo.png", -1)

print(img)  # This will print a numpy array
print(type(img))  # <class 'numpy.ndarray'>

# Image Shape
print(img.shape)
# It gives something like: (995,1000,2)
# where 995 is Height(rows) of numpy array
# where 1000 is Width(cols) of numpy array
# where 3 is Channels of numpy array
