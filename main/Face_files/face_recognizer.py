import cv2
import os
import threading as tr
from pygame import mixer
import subprocess as sub
import time


data_path = 'C:\\Users\\Educa Informatica\\Desktop\\Repos\\Data_face'
image_paths = os.listdir(data_path)

d = dir(cv2)


face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('C:\\Users\\Educa Informatica\\Desktop\\Repos\\Face\\LBPHFaceModel.xml')

face_classif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')


def face_rec(state):
    capture = cv2.VideoCapture(0)##### CAPTURA DE VIDEO
    cont = 0
    while True:
        comp, frame = capture.read()##### LEER CADA FRAME DEL VIDEO
        if comp == False: break

        gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)##### CAPA DE COLOR GRIS
        aux_frame = gray.copy()


        faces = face_classif.detectMultiScale(gray, 1.3, 5)


        for (x, y, w, h) in faces:
            face = aux_frame[y:y+h, x:x+w]
            face = cv2.resize(face, (150, 150), interpolation=cv2.INTER_CUBIC)#REESTABLECER SIZE A 150 Y 150


            result = face_recognizer.predict(face)# PREDICT DE LOS ROSTROS ENCONTRADOS EN LA CAMARA CON EL MODELO ENTRENADO
            
            cv2.putText(frame, f'{result}', (x, y-5), 1, 1.3, (255, 255, 0), 1,cv2.LINE_AA)
            
            

            if result[1] < 76: # MAYOR DE 76 NO COINCIDEN LOS ROSTROS

                if result[0] == 0:
                    cv2.putText(frame, f'{image_paths[0]}',(x, y-25), 2, 1.1, (0,255, 0),lineType= cv2.LINE_AA)# NOMBRE DEL SUJERO/A
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)# RECTANGULO DE COLOR VERDE AL ROSTRO
                elif result[0] == 1:
                    cv2.putText(frame, f'{image_paths[1]}',(x, y-25), 2, 1.1, (0,255, 0))
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        

            else:
                
                cv2.putText(frame, 'Desconocido', (x, y-20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                thread_alarma_song(state, cont)
                

        cv2.imshow('frame', frame)

        cont += 1

        if cv2.waitKey(1) == 27:
            sub.call(f'taskkill /IM python.py /F', shell = True)
            capture.release()
            cv2.destroyAllWindows()
            break
            
    



def alarma_song(state, cont):
    if state == 0 and cont > 10:
        #winsound.PlaySound('C:\\Users\\Educa Informatica\\Desktop\\Repos\\sonidos\\Spaceship.mp3', winsound.SND_FILENAME)
        mixer.music.load('C:\\Users\\Educa Informatica\\Desktop\\Repos\\sonidos\\Spaceship.mp3')
        mixer.music.play()
        time.sleep(5)
        mixer.stop()
       

def thread_alarma_song(state, cont):
    mixer.init()
    ta = tr.Thread(target=alarma_song, args=(state, cont, ))
    ta.start()


