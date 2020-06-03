from claseNodo import Nodo
from interfazLista import ILista

from zope.interface import implementer

@implementer(ILista)
class Lista(object):
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__actual = None

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            elemento = self.__actual.getElemento()
            self.__actual = self.__actual.getSiguiente()
            return elemento

    def insertarElemento(self, posicion, elemento):
        try:
            int(posicion)
        except ValueError:
            raise Exception('La posicion debe ser un valor entero.')
        else:
            posicion = int(posicion)

        if posicion < 0 or posicion > self.__tope:
            raise Exception('Indice fuera de rango.')
        else:
            if posicion == 0:
                nuevo = Nodo(elemento)
                nuevo.setSiguiente(self.__comienzo)
                self.__comienzo = nuevo
                self.__actual = self.__comienzo
                self.__tope += 1
            else:
                while self.__indice <= posicion:
                    if self.__indice == posicion - 1:
                        anterior = self.__actual
                    if self.__indice == posicion:
                        nuevo = Nodo(elemento)
                        nuevo.setSiguiente(self.__actual)
                        anterior.setSiguiente(nuevo)
                        self.__actual = nuevo
                        self.__tope += 1
                    self.__actual = self.__actual.getSiguiente()
                    self.__indice += 1
                self.__indice = 0
                self.__actual = self.__comienzo

    def agregarElemento(self, elemento):
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
    
    def mostrarElemento(self, posicion):
        try:
            int(posicion)
        except ValueError:
            raise Exception('La posicion debe ser un valor entero.')
        else:
            posicion = int(posicion)

        if posicion < 0 or posicion > self.__tope:
            raise Exception('Indice fuera de rango.')
        
        while self.__indice <= posicion:
            if self.__indice == posicion:
                elemento = self.__actual.getElemento()
            self.__actual = self.__actual.getSiguiente()
            self.__indice += 1
        
        self.__actual = self.__comienzo
        self.__indice = 0
        return type(elemento)

    
