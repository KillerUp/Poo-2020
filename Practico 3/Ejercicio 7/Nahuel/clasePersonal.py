import abc
from abc import ABC
class Personal():
    __cuil = ''
    __apellido = ''
    __nombre = ''
    __sueldo = 0.0
    __antiguedad = 0


    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad):
        if not cuil.isnumeric():
            raise Exception("El CUIL no puede contener letras o caracteres especiales.")
        else:
            cuil = '{}-{}-{}'.format(cuil[0:2], cuil[2:len(cuil) - 1], cuil[len(cuil) - 1])
        if not apellido.isalpha():
            raise Exception("El apellido no puede contener numeros ni caracteres especiales.")
        if not nombre.isalpha():
            raise Exception("El anombre no puede contener numeros ni caracteres especiales.")
        
        try:
            self.__sueldo = float(sueldo)
        except:
            raise Exception("El sueldo debe ser un numero entero o real.")
        try:
            self.__antiguedad = int(antiguedad)
        except:
            raise Exception("La antiguedad debe ser un numero entero.")
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre



    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getSueldo(self):
        return self.__sueldo

    def toJSON(self):
        diccionario = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = self.__cuil.replace('-', ''),
                apellido = self.__apellido,
                nombre = self.__nombre,
                sueldo = self.__sueldo,
                antiguedad = self.__antiguedad
            )
        )
        return diccionario
    
    def calcularSueldo(self):
        return self.__sueldo + (self.__antiguedad * self.__sueldo / 100)
    
    def __gt__(self, otro):
        return self.__apellido > otro.getApellido()

    def __str__(self):
        cadena = "CUIL: {}\nApellido: {}\nNombre: {}\nSueldo: {}\nAntiguedad: {}\n".format(
            self.__cuil,
            self.__apellido,
            self.__nombre,
            self.calcularSueldo(),
            self.__antiguedad
        )
        return cadena