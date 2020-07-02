import json
from pathlib import Path

from Lista import Lista
from claseProvincia import Provincia


class ObjectEncoder(object):

    __archivo = ''

    def __init__(self, archivo):
        self.__archivo = archivo

    def leer(self):
        with Path(self.__archivo).open(encoding = "UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
        return diccionario

    def guardar(self,provincias):
        with open(self.__archivo, 'w', encoding = "UTF-8") as destino:
            json.dump(provincias,destino, indent=3)
        destino.close()

    def decoder(self,d):
        if '__class__' not in d:
            return d
        else:
            class_name = d["__class__"]
            class_ = eval(class_name)
            if class_name == 'Lista':
                provincias = d["datos"]
                la_lista = class_()
                for i in range(len(provincias)):
                    dprovincia = provincias[i]
                    class_name = dprovincia.pop("__class__")
                    class_ = eval(class_name)
                    atributos = dprovincia['__atributos__']
                    una_provincia = class_(**atributos)
                    la_lista.agregarElemento(una_provincia)
        return la_lista
