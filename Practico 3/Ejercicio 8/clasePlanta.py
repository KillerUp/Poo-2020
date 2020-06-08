from claseEmpleado import Empleado


class Planta(Empleado):
    __sueldo_basico = 0.0
    __antiguedad = 0

    def __init__(self, dni = 0, nombre = '', direccion = '', telefono = 0, sueldo = 0.0, antiguedad = 0):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldo_basico = float(sueldo)
        self.__antiguedad = int(antiguedad)

    def calculaSueldo(self):
        sueldo = self.__sueldo_basico + ((self.__sueldo_basico + self.__antiguedad) / 100)
        return sueldo

    def __eq__(self, otro):
        return type(self) == type(otro)

    def modifica(self,dinero):
        self.__sueldo_basico = dinero