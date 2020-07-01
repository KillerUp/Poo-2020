import json
from pathlib import Path

from Lista import Lista
from Paciente import Paciente


class ObjectEncoder(object):

    __archivo = ''

    def __init__(self, archivo):
        self.__archivo = archivo

    def leer(self):
        with Path(self.__archivo).open(encoding = "UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
        return diccionario

    def guardar(self,pacientes):
        with open(self.__archivo, 'w', encoding = "UTF-8") as destino:
            json.dump(pacientes,destino, indent=3)
        destino.close()

    def decoder(self,d):
        if '__class__' not in d:
            return d
        else:
            class_name = d["__class__"]
            class_ = eval(class_name)
            if class_name == 'Lista':
                pacientes = d["datos"]
                la_lista = class_()
                for i in range(len(pacientes)):
                    dpaciente = pacientes[i]
                    class_name = dpaciente.pop("__class__")
                    class_ = eval(class_name)
                    atributos = dpaciente['__atributos__']
                    un_paciente = class_(**atributos)
                    la_lista.agregarElemento(un_paciente)
        return la_lista
