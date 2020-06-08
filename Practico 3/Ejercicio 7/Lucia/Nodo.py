from Agentes import Agentes

class Nodo(object):
    __agente = None
    __siguiente = None

    def __init__(self,agente):
        self.__agente = agente
        self.__siguiente = None

    def NodoSiguiente(self,siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getAgente(self):
        return self.__agente
