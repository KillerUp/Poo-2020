import json
from Lista import Lista
from Agentes import Agentes
from Docentes import Docentes
from DocenteInvestigador import DocenteInvestigador
from Investigador import Investigador
from PersonalApoyo import PersonalApoyo
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
                agentes = d["datos"]
                la_lista = class_()
                for i in range(len(agentes)):
                    dagente = agentes[i]
                    class_name = dagente.pop("__class__")
                    class_ = eval(class_name)
                    atributos = dagente['__atributos__']
                    un_agente = class_(**atributos)
                    la_lista.agregarElemento(un_agente)
        return la_lista

