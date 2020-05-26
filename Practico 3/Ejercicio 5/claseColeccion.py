from interfazColeccion import IColeccion

from zope.interface import implementer


@implementer(IColeccion)
class Coleccion(object):
    __coleccion = []

    def __init__(self):
        self.__coleccion = []

    def insertarElemento(self, posicion, elemento):
        try:
            int(posicion)
        except ValueError:
            raise Exception('La posicion debe ser un valor entero.')
        else:
            posicion = int(posicion)

        if posicion < 0 or posicion > len(self.__coleccion):
            raise Exception('Indice fuera de rango.')
        else:
            self.__coleccion.insert(posicion, elemento)

    def agregarElemento(self, elemento):
        self.__coleccion.append(elemento)

    def mostrarElemento(self, posicion):
        try:
            int(posicion)
        except ValueError:
            raise Exception('La posicion debe ser un valor entero.')
        else:
            posicion = int(posicion)
        
        if posicion < 0 or posicion > len(self.__coleccion):
            raise Exception('Indice fuera de rango.')
        else:
            print(self.__coleccion[posicion])