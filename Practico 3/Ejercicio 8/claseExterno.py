from claseEmpleado import Empleado
import datetime as dt

class Externo(Empleado):
    __tarea = ''
    __monto_viatico = 0.0
    __costo_de_obra = 0.0
    __seguro_de_vida = 0.0
    
    def __init__(self, dni, nombre, direccion, telefono, tarea,fecha_ini, fecha_fin, viatico, costo_obra, seguro):
        super().__init__(dni, nombre, direccion, telefono)
        self.__monto_viatico = float(viatico)
        self.__costo_de_obra = float(costo_obra)
        self.__seguro_de_vida = float(seguro)
        self.__fecha_inicio = dt.date.fromisoformat(fecha_ini)
        self.__fecha_finalizacion = dt.date.fromisoformat(fecha_fin)
        self.__tarea = tarea


    def __eq__(self, otro):
        return type(self) == type(otro)

    def getTarea(self):
        return self.__tarea

    def getFechaFin(self):
        return self.__fecha_finalizacion

    def calculaSueldo(self):
        sueldo = self.__costo_de_obra - self.__monto_viatico - self.__seguro_de_vida
        return sueldo

    def modifica (self,dinero):
        self.__monto_viatico = dinero