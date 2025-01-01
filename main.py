import cv2
import time
import email

video = cv2.VideoCapture(1) #captures main camera with 0 and external and virtual camera with 1

first_frame = None

status_list = [0]

while True:
    status = 0
    check,frame = video.read()

    grey_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    grey_gau = cv2.GaussianBlur(grey_frame,(21,21),0)
    time.sleep(0)


    if first_frame is None:
        first_frame = grey_frame

    delta_frame = cv2.absdiff( first_frame , grey_frame) # show changes in frame

    thresh_frame = cv2.threshold(delta_frame,45,255,cv2.THRESH_BINARY)[1] # makes difference bigger

    dil_frame = cv2.dilate(thresh_frame,None,iterations=2)  # makes the thresh bigger

    contours, check = cv2.findContours(dil_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # detects outer shape of changed areas

    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue

        x,y,w,h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame,(x,y),(x+w,y+h), (0,225,0))
        if rectangle.any():
            status = 1

    status_list.append(status)
    status_list = status_list[-2:]

    print(status_list)

    if status_list[0] == 0 and status_list[1] == 1:
        email.email_send()

    cv2.imshow("My video", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()