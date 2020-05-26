import numpy as np
from ClaseTaller import TallerCapacitacion
import csv

class ArregloTaller:

    __dimension = 0
    def __init__(self):
        self.__arreglo = np.empty(self.__dimension, dtype = TallerCapacitacion)

    def carga(self):
        i = 0
        archivo = open('Talleres.csv')
        reader = csv.reader(archivo, delimiter = ',')
        ban = True
        for linea in reader:
            if ban:
                self.__dimension = int(linea[0])
                self.__arreglo.resize(self.__dimension)
                ban = False
            else:
                taller = TallerCapacitacion(*linea)
                self.__arreglo[i] = taller
                i += 1
        archivo.close()

    def mostrar(self):
        for i in range(self.__dimension):
            print(self.__arreglo[i])

    def buscarporID(self, id_taller):
        i = 0
        while i <= self.__dimension:
            if id_taller == self.__arreglo[i].getID():
                return True
            else:
                i+=1
        return False

    def buscarpornombre(self, nombre):
        i = 0
        while i <= self.__dimension:
            if nombre.lower() == self.__arreglo[i].getNombre().lower():
                return self.__arreglo[i]
            else: 
                i+=1        
        return None

    def modifica(self,id_taller):
        i = 0 
        ban = True
        while (ban == True) and (i <= self.__dimension):
            if self.__arreglo[i].getID() == id_taller:
                self.__arreglo[i].modificaVacante()
                ban = False
            else:
                i+=1



