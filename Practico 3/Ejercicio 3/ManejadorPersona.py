from ClasePersona import Persona

class Manejador:
    __lista = []

    def __init__(self):
        self.__lista = []

    def agrega(self,persona):
        self.__lista.append(persona)

