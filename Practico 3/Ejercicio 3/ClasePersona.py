class Persona:
    __nombre = ''
    __direccion = ''
    __dni = 0

    def __init__(self,nombre,direccion,dni):
        self.__nombre = nombre
        self.__direccion =  direccion
        self.__dni = dni
    
    def getdni(self):
        return self.__dni

    def getDatos(self):
        return(self.__nombre,self.__dni,self.__direccion)
