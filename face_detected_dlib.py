import cv2 as cv
import dlib 
from scipy.spatial import distance as dist #para calculos geométricos e espaciais
import numpy as np

def Identify_Face(webcam):
    face_detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    while True:
        isTrue, frame = webcam.read()
        frame = cv.flip(frame,1)
    
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        faces = face_detector(gray)
        print(f"Quantidade de Rostos: {len(faces)}")
        DefinePoints(faces,predictor,gray,frame)

        cv.imshow("Deteccao de olhos com o Dlib.",frame)
        if cv.waitKey(20) & 0xFF==ord('c'):
            break

    webcam.release()
    cv.destroyAllWindows()



def DefinePoints(faces,predictor,gray,frame):
    for face in faces:
        landmarks = predictor(gray,face) #Prevê e cria os 68 pontos no rosto
        Identify_Eyes(landmarks,frame)

def Identify_Eyes(landmarks,frame):


    left_eye = np.array([landmarks.part(i) for i in range(36, 42)]).ravel()
    right_eye = np.array([landmarks.part(i) for i in range(42, 48)]).ravel()



    for i in range(36,42):
        x = landmarks.part(i).x
        y = landmarks.part(i).y
        cv.circle(frame,(x,y),1,(0,255,0),-1)

    for i in range(42,48):
        x = landmarks.part(i).x
        y = landmarks.part(i).y
        cv.circle(frame,(x,y),1,(0,255,0),-1)
    
    left_ratio = Area_Eyes(left_eye)
    right_ratio = Area_Eyes(right_eye)

    Sleep_Detected(left_ratio,right_ratio,frame)

def Area_Eyes(eye):
    # Por meio da distância euclidiano dos landmarks dos olhos teremos a área dos olhos abertos
    A = dist.euclidean((eye[1].x, eye[1].y), (eye[5].x, eye[5].y))
    B = dist.euclidean((eye[2].x, eye[2].y), (eye[4].x, eye[4].y))
    C = dist.euclidean((eye[0].x, eye[0].y), (eye[3].x, eye[3].y))

    eye_ratio = (A + B) / (2.0 * C)

    return eye_ratio

def Sleep_Detected(left_ratio,right_ratio,frame):
    EYE_AR_THRESH = 0.25
    # Frames with eyes closed
    EYE_AR_CONSEC_FRAMES = 10
    
    close_left_eye = 0
    close_right_eye = 0
    
    if left_ratio < EYE_AR_THRESH:
        close_left_eye +=1

    if right_ratio < EYE_AR_THRESH:
        close_right_eye += 1
    
    if (close_right_eye != 0) and (close_left_eye != 0):
        print("Ambos olhos fechados")
        cv.putText(frame, "Olhos fechados!!",(10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        

webcam = cv.VideoCapture(0)
Identify_Face(webcam)