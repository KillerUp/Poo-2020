import csv

from Clases import ViajeroFrecuente

class Manejadorlista(object):
    __lista = []
    def __init__(self):
        self.__lista = []

    def cargalista(self):
        archivo = open('Practico 1/Ejercicio 2/Viajeros.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for linea in reader:
            aux = ViajeroFrecuente((linea[0]), linea[1], linea[2], linea[3], linea[4])
            self.__lista.append(aux)
        pass

    def buscar(self, num = 0):
        for i in range(len(self.__lista)):
            if self.__lista[i].esViajero(num) == 1:
                return i
        else:
            return(-1)
        pass

    def acum(self, millas = 0, numviaj = 0):
        i = self.buscar(numviaj)
        if i == -1:
            print('Viajero no encontrado')
        else:
            self.__lista[i].acumularMillas(millas)

    def canj(self, millas = 0, numviaj = 0):
        i = self.buscar(numviaj)
        if i == -1:
            print('Viajero no encontrado')
        else:
            self.__lista[i].canjearMillas(millas)
    
    def millas(self, numviaj):
        i = self.buscar(numviaj)
        if i == -1:
            print('Viajero no encontrado')
        else:
            return self.__lista[i].cantidadTotaldeMillas()
        pass
    def get_lista(self):
        return self.__lista