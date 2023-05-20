import cv2
import face_recognition
import pickle
import os

images = []
persons = []

for path in os.listdir('./images/persons'):
    if(os.path.splitext(path)[0] != '.DS_Store'):
        images.append(cv2.imread(os.path.join('./images/persons',path)))
        persons.append(os.path.splitext(path)[0])
    
def findEncodings(images):
    encodes = []
    for image in images:
        encodes.append(face_recognition.face_encodings(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))[0])
    return encodes
        
file = open('encode.p','wb')
pickle.dump([findEncodings(images),persons],file)
file.close()