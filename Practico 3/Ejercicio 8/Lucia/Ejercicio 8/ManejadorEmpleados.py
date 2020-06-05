from claseContratado import Contratado
from claseEmpleado import Empleado
from claseExterno import Externo
from clasePlanta import Planta
import datetime as dt
from zope.interface import implementer
from InterfazTesorero import ITesorero
from InterfazGerente import IGerente
import csv
import numpy as np
@implementer(ITesorero)
@implementer(IGerente)

class ManejadorEmpleados(object):
    __dimension = 0

    def __init__(self, cantidad_empleados):
        self.__empleados = np.empty(cantidad_empleados, dtype=Empleado)
        self.__dimension = cantidad_empleados
    
    def cargarEmpleados(self):
        i = 0

        e = open('Practico 3/Ejercicio 4/externo.csv')
        reader = csv.reader(e, delimiter = ',')
        for linea in reader:
            o = Externo(*linea)
            self.__empleados[i] = o
            i+=1
        
        e.close()

        c = open('Practico 3/Ejercicio 4/contratados.csv')
        reader = csv.reader(c, delimiter = ',')
        for linea in reader:
            o = Contratado(*linea)
            self.__empleados[i] = o
            i+=1
        
        c.close()

        f = open('Practico 3/Ejercicio 4/planta.csv')
        reader = csv.reader(f, delimiter = ',')
        for linea in reader:
            o = Planta(*linea)
            self.__empleados[i] = o
            i+=1
        
        f.close()

    def RegistrarHoras(self,dni,horas):
        i = 0
        ban = False
        while i < self.__dimension and ban == False:
            if int(self.__empleados[i].getDni()) == dni:
                if type(self.__empleados[i]) == Contratado:
                    self.__empleados[i].registro(horas)
                    ban = True
                else: 
                    print("El empleado no trabaja por horas")
                    ban = True
            else:
                i+=1    

    def MostrarMonto(self, tarea, fecha):
        i = 0
        monto = 0.0
        while i < self.__dimension:
            if type(self.__empleados[i]) == Externo:
                if self.__empleados[i].getTarea().upper() == tarea.upper():
                    if fecha > self.__empleados[i].getFechaFin():
                        monto += self.__empleados[i].calculaSueldo()
                        i += 1
                    else:
                        i += 1
                else: 
                    i += 1
            else:
                i += 1
        return monto

    def ayudaSolidaria(self):
        for empleado in self.__empleados:
            if empleado.calculaSueldo() < 25000:
                print(empleado)
        
    def mostrarSueldos(self):
        for empleado in self.__empleados:
            print('Nombre: {}\nTelefono: {}\nSueldo: {}\n'.format(empleado.getNombre(), empleado.getTelefono(), round(empleado.calculaSueldo(), 2)))

    def gastosSueldoPorEmpleado(self,dni):
        i = 0
        while i < self.__dimension:
            if int(self.__empleados[i].getDni()) == int(dni):
                sueldo = self.__empleados[i].calculaSueldo()
                return sueldo
            else:
                i+=1   
        return None

    def modificarBasicoEPlanta(self,dni,nuevoBasico): 
        i = 0
        ban = False
        while i < self.__dimension and ban == False:
            if int(self.__empleados[i].getDni()) == int(dni):
                if isinstance(self.__empleados[i],Planta):
                    self.__empleados[i].modifica(nuevoBasico)
                    ban = True
                else: 
                    print("El empleado no trabaja en planta")
                    ban = True
            else:
                i+=1    

    def modificarViaticoEExterno(self,dni,nuevoViatico):
        i = 0
        ban = False
        while i < self.__dimension and ban == False:
            if int(self.__empleados[i].getDni()) == int(dni):
                if isinstance(self.__empleados[i],Externo):
                    self.__empleados[i].modifica(nuevoViatico)
                    ban = True
                else: 
                    print("El empleado no trabaja en Externo")
                    ban = True
            else:
                i+=1

    def modificarValorEPorHora(self,dni,nuevoValorHora):
        i = 0
        ban = False
        while i < self.__dimension and ban == False:
            if int(self.__empleados[i].getDni()) == int(dni):
                if isinstance(self.__empleados[i],Contratado):
                    self.__empleados[i].modifica(nuevoValorHora)
                    ban = True
                else: 
                    print("El empleado no trabaja por hora")
                    ban = True
            else:
                i+=1

    
