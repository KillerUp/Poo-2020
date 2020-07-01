import re


class Paciente(object):
    telefonoRegex = re.compile(r"\([0-9]{3}\)[0-9]{7}")
    __nombre = ''
    __apellido = ''
    __telefono = 0
    __altura = 0.0
    __peso = 0.0

    def __init__(self,nombre,apellido,telefono,altura,peso):
        self.__apellido = self.requerido(apellido, 'Apellido es un valor requerido')
        self.__nombre = self.__nombre=self.requerido(nombre, 'Nombre es un valor requerido')
        self.__telefono = self.formatoValido(telefono, Paciente.telefonoRegex, 'Teléfono no tiene formato correcto')
        self.__altura = self.requerido(altura, 'Altura es un valor requerido')
        self.__peso = self.requerido(peso, 'Peso es un valor requerido')

    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def formatoValido(self, valor, regex, mensaje):
        if not valor or not regex.match(valor):
            raise ValueError(mensaje)
        return valor

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__= dict(
                nombre = self.__nombre,
                apellido = self.__apellido,
                telefono = self.__telefono,
                altura = self.__altura,
                peso = self.__peso
                )
                )
        return d

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getTelefono(self):
        return self.__telefono

    def getAltura(self):
        return self.__altura

    def getPeso(self):
        return self.__peso

    def __str__(self):
        return '{} {}'.format(self.__nombre.capitalize(), self.__apellido.capitalize())
