import datetime as dt
from ManejadorEmpleados import ManejadorEmpleados

class Menu(object):
    __switcher=None
    def __init__(self):
        self.__switcher = {
            '1' : self.opcion1,
            '2' : self.opcion2,
            '3' : self.opcion3,
            '4' : self.opcion4,
            'x' : self.salir
            }
            
        tamaño = int(input("Ingrese la cantidad de empleados: "))
        self.__arreglo = ManejadorEmpleados(tamaño)
        self.__arreglo.cargarEmpleados()
        
        
    def funcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print("Fin del prograrma.")

    def opcion1(self):
        dni = int(input("Ingrese su dni: "))
        horas = int(input("Ingrese la cantidad de horas trabajadas: "))
        self.__arreglo.RegistrarHoras(dni,horas)

    def opcion2(self):
        tarea = input ("Ingrese la tarea que realiza: ")
        fecha = dt.date.today()
        print('Tarea: {}\nMonto a pagar: {}'.format(tarea, self.__arreglo.MostrarMonto(tarea,fecha)))

    def opcion3(self):
        print("Empleados que reciben la ayuda:")
        self.__arreglo.ayudaSolidaria()

    def opcion4(self):
        self.__arreglo.mostrarSueldos()
    