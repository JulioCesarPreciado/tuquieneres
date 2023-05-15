import cv2
import random

class Helper:
    #Función para crear el rectangulo de las caras.
    def rectangle(self, coords):
        return 10 + (coords[3] * 4), 10 + (coords[0] * 4), (coords[1] * 4) - (coords[3] * 4), (coords[2] * 4) - (coords[0] * 4)
    #Funcion para borrar texto
    def remove(self,bg):
        cv2.rectangle(bg,(890,128),(1232,590),(255, 255, 255), -1)
    #Funcion para poner imagenes
    def putImage(self, bg, path):
        bg[228:428,975:1175] = cv2.imread(path)
    #Función para poner el titulo de las imagenes
    def putText(self, bg, text):
        cv2.putText(bg, text, (970, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
    #Función para dar un número aleatorio
    def random(self,start,end):
        return str(random.randint(start, end))
        
    