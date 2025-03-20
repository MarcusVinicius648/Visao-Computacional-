import cv2 as cv
import dlib 

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
    for i in range(36,42):
        x = landmarks.part(i).x
        y = landmarks.part(i).y
        cv.circle(frame,(x,y),1,(0,255,0),-1)

    for i in range(32,48):
        x = landmarks.part(i).x
        y = landmarks.part(i).y
        cv.circle(frame,(x,y),1,(0,255,0),-1)


webcam = cv.VideoCapture(0)
Identify_Face(webcam)