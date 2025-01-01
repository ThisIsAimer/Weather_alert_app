import cv2
import time

video = cv2.VideoCapture(1) #captures main camera with 0 and external and virtual camera with 1

first_frame = None

while True:
    check,frame = video.read()

    grey_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    grey_gau = cv2.GaussianBlur(grey_frame,(21,21),0)
    time.sleep(0)


    if first_frame is None:
        first_frame = grey_frame

    delta_frame = cv2.absdiff( first_frame , grey_frame)

    cv2.imshow("My video", delta_frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()