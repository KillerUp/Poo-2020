from claseLista import Lista
from claseNuevo import Nuevo
from claseUsado import Usado

import json


class objetEncoder(object):
    def __init__(self):
        pass

    def decodificar(self, dicc):
        if '__class__' in dicc:
            return dicc
        else:
            lista = Lista()
            for vehiculo in dicc['vehiculos']:
                clase = vehiculo['__class__']
                clase_ = eval(clase)
                if clase == 'Nuevo':
                    obj = clase_(**vehiculo['__atributos__'])
                    lista.agregarElemento(obj)
                else:
                    obj = clase_(**vehiculo['__atributos__'])
                    lista.agregarElemento(obj)
        return lista

    def leerJSON(self, archivo):
        with open(archivo, 'r', encoding='UTF-8') as f:
            dicc = json.load(f)
            f.close()
        return dicc
        
    def guardarJSON(self, archivo, dicc):
        with open(archivo, 'w', encoding='UTF-8') as f:
            dicc = json.dump(dicc, f, indent=3)
            f.close()