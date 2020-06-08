import abc
from abc import ABC


class Vehiculo(ABC):
    __modelo = ''
    __puertas = 0
    __color = ''
    __precio = 0.0

    def __init__(self, modelo, puertas, color, precio):
        self.__modelo = str(modelo).capitalize()
        self.__puertas = int(puertas)
        self.__color = str(color).lower()
        self.__precio = float(precio)
    
    @abc.abstractclassmethod
    def calcularImporte(self):
        pass

    def getModelo(self):
        return self.__modelo
    
    def getPuertas(self):
        return self.__puertas