import cv2
import time

video = cv2.VideoCapture(1) #captures main camera with 0 and external and virtual camera with 1


while True:
    check,frame = video.read()
    time.sleep(0)
    cv2.imshow("My video" , frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()