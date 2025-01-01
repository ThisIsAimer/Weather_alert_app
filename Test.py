import cv2
import numpy

# array = cv2.imread("image.png")
#
# print(array.shape)
# print(array)

#-------------------------------- making images-----------------------------------

# img_data = numpy.array(
# [[[255,   0,   0],
#   [255, 255, 255],
#   [255, 255, 255],
#   [187, 41, 160]],
#
#  [[255, 255, 255],
#   [255, 255, 255],
#   [255, 255, 255],
#   [255, 255, 255]],
#
#  [[255, 255, 255],
#   [  0,   0,   0],
#   [ 47, 255, 173],
#   [255, 255, 255]]])
#
# cv2.imwrite("img2.png", img_data)



import cv2
import time

video = cv2.VideoCapture(0)

check , frame = video.read()

print(check)