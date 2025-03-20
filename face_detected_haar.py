import numpy as np
import cv2 as cv
import os 

def TakeImage(webcam):
    while True:
        istrue, frame = webcam.read()
        flip = cv.flip(frame,1)
        gray,faces_rect = Identify_Face(flip)
        frame_rect = flip

        if len(faces_rect) != 0:
            frame_rect = Rectangle_Face(faces_rect,flip,gray)

        print(f"Number of Faces Found = {len(faces_rect)}")
        cv.imshow("Computer webcam", frame_rect) 

        if cv.waitKey(20) & 0xFF==ord('c'):
            break

    webcam.release()
    cv.destroyAllWindows()


# Haar cascade identify based on edge 
def Identify_Face(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_haar_cascade = cv.CascadeClassifier('Cascades/haar_face.xml')

    faces_rect = face_haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4) # minNeighbors is to setup how sensite you need your aplication

    return gray,faces_rect


def Identify_Eyes(roi_gray,roi_frame):
    eye_haar_cascade = cv.CascadeClassifier('Cascades/haarcascade_eye.xml')
    eyes = eye_haar_cascade.detectMultiScale(roi_gray, scaleFactor= 1.1, minNeighbors=10,)
    print(f'Número de olhos: {len(eyes)}')
    Rectangle_Eye(eyes,roi_frame)


def Rectangle_Face(faces_rect,frame,gray):
    for(x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_frame = frame[y:y+h, x:x+w]
        Identify_Eyes(roi_gray,roi_frame)

        return frame


def Rectangle_Eye(eyes,roi_frame):
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_frame, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), thickness=2)


webcam = cv.VideoCapture(0)
TakeImage(webcam)