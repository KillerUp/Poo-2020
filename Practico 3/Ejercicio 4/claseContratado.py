from claseEmpleado import Empleado
import datetime as dt


class Contratado(Empleado):
    __valor_hora = 0.0
    __horas_trabajadas = 0

    def __init__(self,dni = 0, nombre = '', direccion = '', telefono = 0, horas = 0, fecha_ini  = '2020-01-01', fecha_fin = '2020-01-01', valor_hora = 0.0):
        super().__init__(dni, nombre, direccion, telefono)
        self.__horas_trabajadas = int(horas)
        self.__valor_hora = float(valor_hora)
        self.__fecha_inicio = dt.date.fromisoformat(fecha_ini)
        self.__fecha_finalizacion = dt.date.fromisoformat(fecha_fin)

    def calculaSueldo(self):
        sueldo = self.__horas_trabajadas * self.__valor_hora
        return sueldo

    def registro(self,horas):
        self.__horas_trabajadas += horas

    def __eq__(self, otro):
        return type(self) == type(otro)