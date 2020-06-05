
class Agentes (object):
    __cuil = 0
    __apellido = ''
    __nombre = ''
    __sueldoBasico = 0.0
    __antiguedad = 0

    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoBasico = sueldoBasico
        self.__antiguedad = antiguedad

    def toJSON (self):
        pass

    def calcularSueldo(self):
        pass

    def __gt__(self, otro):
        return self.__apellido > otro.__apellido
    
    def __str__(self):
        pass
