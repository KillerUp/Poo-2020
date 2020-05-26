from claseColeccion import Coleccion
from interfazColeccion import IColeccion


class Menu(object):
    __switcher=None
    def __init__(self):
        self.__switcher = {
            '1' : self.opcion1,
            '2' : self.opcion2,
            '3' : self.opcion3,
            'x' : self.salir
            }
        self.__mc = Coleccion()
    def funcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print("Fin del prograrma.")

    def opcion1(self):
        dato = input('Ingrese el dato que decea insertar: ')
        pos = (input('Ingrese la posicion donde quiere insertar el dato: '))

        IColeccion(self.__mc).insertarElemento(pos, dato)
        pass

    def opcion2(self):
        dato = input('Ingrese el dato que decea insertar: ')
        IColeccion(self.__mc).agregarElemento(dato)
        pass

    def opcion3(self):
        pos = (input('Ingrese la posicion donde quiere insertar el dato: '))
        IColeccion(self.__mc).mostrarElemento(pos)
        pass