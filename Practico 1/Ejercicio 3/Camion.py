class Camion:
    __id = ''
    __conductor = ''
    __patente = ''
    __marca = ''
    __tara = ''
    
    def __init__(self, idcamion ='', conductor = '', patente = '', marca = '', tara = ''):
        self.__id = idcamion
        self.__conductor = conductor
        self.__patente = patente
        self.__marca = marca
        self.__tara = tara
        pass

    def getDatos(self):
        return(self.__patente, self.__conductor.capitalize())

