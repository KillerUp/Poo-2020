import json
from Coleccion import Lista
from VehiculoNuevo import VehiculoNuevo
from VehiculoUsado import VehiculoUsado
from pathlib import Path


class ObjectEncoder(object):

    def leer(self, archivo):
        with Path(archivo).open(encoding = "UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
        return diccionario

    def guardar(self,vehiculos,archivo):
        with open(archivo, 'w', encoding = "UTF-8") as destino:
            json.dump(vehiculos,destino)
        destino.close()

    def decoder(self,d):
        if "__class__" not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'Lista':
                vehiculos = d["datos"]
                la_lista = class_()
                for i in range(len(vehiculos)):
                    dvehiculo = vehiculos[i]
                    class_name = dvehiculo.pop("__class__")
                    class_ = eval(class_name)
                    atributos = dvehiculo['__atributos__']
                    un_vehiculo = class_(**atributos)
                    la_lista = Lista() 
                    la_lista.agregarElemento(un_vehiculo)
        return la_lista

