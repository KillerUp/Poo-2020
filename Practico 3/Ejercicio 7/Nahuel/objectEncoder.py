import json

from claseApoyo import Apoyo
from claseDocente import Docente
from claseDocenteInvestigador import DocenteInvestigador
from claseInvestigador import Investigador
from claseLista import Lista


class objetEncoder(object):
    def __init__(self):
        pass

    def decodificar(self, dicc):
        if '__class__' in dicc:
            return dicc
        else:
            lista = Lista()
            for persona in dicc['personal']:
                clase = eval(persona['__class__'])
                obj = clase(**persona['__atributos__'])
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
