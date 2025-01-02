import cv2
import streamlit

from app import frame

streamlit.title("Webcam alert app")
start = streamlit.button("Start Button")


if start:
    streamlit_image = streamlit.image([])
    camera1 = cv2.VideoCapture(1)

    while True:

        check, frame = camera1.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        cv2.putText(frame,text="opening cam",org=(50,50),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(0,250,0),thickness=2,lineType=cv2.LINE_AA)

        streamlit_image.image(frame)

