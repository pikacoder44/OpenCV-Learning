import cv2

img = cv2.imread("assets/logo.png", -1)

# print(img)  # This will print a numpy array
# print(type(img))  # <class 'numpy.ndarray'>

# Image Shape
print(img.shape)
# It gives something like: (995,1000,2)
# where 995 is Height(rows) of numpy array
# where 1000 is Width(cols) of numpy array
# where 3 is Channels of numpy array


# RGB vs BGR
# Standard is RGB - OpenCV uses BGR (Blue, Green, Red)
# when we get [10,20,30] as array we get it as:
# 10 = Blue , 20 = Green, 30 = Red


# Accessing Pixel Values

# print(img[0])  # this gives us first row
# print(img[257][45:400]) # print pixels on 257th row between 45th pixel to 400th pixel

print(img[257][400]) # prints 400th pixel on 257th row
