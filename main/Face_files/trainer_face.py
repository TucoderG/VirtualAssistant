import os
import numpy as np
import cv2


d = dir(cv2)



data_path = 'Data_Face'
people = os.listdir(data_path)
print(people)
labels = []
face_data = []
label = 0

for person in people:
    person_path = data_path + '/' + person
    print('Leyendo las imagenes')
    for file_name in os.listdir(person_path):
        print(f'Faces: {person}/{file_name}')
        labels.append(label)
        face_data.append(cv2.imread(person_path + '/' + file_name, 0))
        
    label+=1

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
print('Entrenando...')
face_recognizer.train(face_data, np.array(labels))

face_recognizer.write('C:\\Users\\Educa Informatica\\Desktop\\Repos\\Face\\LBPHFaceModel.xml')
print('Modelo almacenado')