import cv2
import time,glob,os
import send_mail

def clean_folder():
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)

video = cv2.VideoCapture(1) #captures main camera with 0 and external and virtual camera with 1

first_frame = None
count = 1
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

    thresh_frame = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1] # makes difference bigger

    dil_frame = cv2.dilate(thresh_frame,None,iterations=2)  # makes the thresh bigger

    contours, check = cv2.findContours(dil_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # detects outer shape of changed areas

    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue

        x,y,w,h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame,(x,y),(x+w,y+h), (0,225,0))
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)
            count += 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images)/2)
            avg_img_w_obj = all_images[index]


    status_list.append(status)
    status_list = status_list[-2:]

    print(status_list)

    if status_list[0] == 1 and status_list[1] == 0:
        send_mail.send_mail(avg_img_w_obj)
        clean_folder()


    cv2.imshow("My video", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()