import abc
from abc import ABC
class Vehiculo(object):
    __modelo = ''
    __cantidadPuertas = 0
    __color = ''
    __precioBase = 0.0

    def __init__(self,modelo,cant,color,precio):
        self.__modelo = modelo
        self.__cantidadPuertas = cant
        self.__color = color
        self.__precioBase = precio

    @abc.abstractmethod 
    def calcularImporte(self):
        pass

    @abc.abstractmethod 
    def toJSON(self):
        pass

    @abc.abstractmethod
    def getModelo(self):
        return self.__modelo

    @abc.abstractmethod
    def getPuertas(self):
        return self.__cantidadPuertas

    @abc.abstractmethod
    def getColor(self):
        return self.__color

    @abc.abstractmethod
    def getPrecio(self):
        return self.__precioBase

    @abc.abstractmethod
    def calcularImporte(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass
    @abc.abstractmethod
    def mostrar(self):
        pass



    