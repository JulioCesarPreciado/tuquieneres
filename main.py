import cv2
import pickle
import face_recognition
import cvzone
from helpers.helper import Helper

helper = Helper()

capture = cv2.VideoCapture(0)

capture.set(3, 640)
capture.set(4, 480)

x = 40
y = 120

bg = cv2.imread('./images/assets/background.png')

file = open('encode.p', 'rb')
encodes, persons = pickle.load(file)
file.close()

while True:
    success, img = capture.read()

    cam = cv2.cvtColor(cv2.resize(img, (0, 0), None, 0.25, 0.25), cv2.COLOR_BGR2RGB)
    # Variable que tiene las coordenadas de donde se reconocio una cara
    recognition = face_recognition.face_locations(cam)
    # Variable que tiene el encoding de la cara detectada por la camara.
    face = face_recognition.face_encodings(cam, recognition)
    # Validamos si esta vacio el encoding es por que no detecto ninguna cara.
    if face:
        for index, encode in enumerate(encodes):
            img = cvzone.cornerRect(img, helper.rectangle(recognition[0]), rt=0, colorC=(168, 50, 160))
            if face_recognition.compare_faces(encode, face)[0]:
                helper.remove(bg)
                helper.putText(bg,'Tu eres una')
                helper.putImage(bg,'./images/assets/' + persons[index] + '.png')
    else:
        helper.remove(bg)
        helper.putText(bg,'No se que eres')
        helper.putImage(bg,'./images/assets/' + helper.random(1,23) + '.png')

    height, width, channels = img.shape

    bg[y:y+height, x:x+width] = img

    cv2.imshow("Te estoy viendo", bg)
    cv2.waitKey(1)
