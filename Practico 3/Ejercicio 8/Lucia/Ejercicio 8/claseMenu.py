import datetime as dt
from ManejadorEmpleados import ManejadorEmpleados
from MenuGerente import Gerente
from InterfazTesorero import ITesorero
import os

class Menu(object):
    __switcher=None
    def __init__(self):
        self.__switcher = {
            '1' : self.opcion1,
            '2' : self.opcion2,
            '3' : self.opcion3,
            '4' : self.opcion4,
            '5' : self.opcion5,
            '6' : self.opcion6,
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

    def opcion5(self):
        salir = False
        gerente = Gerente(self.__arreglo)
        usuario = input ("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if usuario == 'uGerente':
            if contraseña == 'ufC77#!1':
                while not salir:
                    print("1) Para modificar el sueldo basico de un empleado de Planta")
                    print("2) Para modificar el viatico de un empleado Extreno")
                    print("3) Para modificar el valor por hora de un empleado Contratado")
                    print("x) Para salir")
                    op = input("Ingrese opcion >> ")
                    os.system("cls") 
                    gerente.funcion(op)
                    salir = bool('x'== op)
                    os.system('pause')
                    os.system("cls")
            else: 
                print("Contraseña incorrecta")
        else:
            print("Ususario incorrecto")

    def opcion6(self):
        salir = False
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if usuario == 'uTesoreso':
            if contraseña == 'ag@74ck':
                while not salir:
                    print("1) Para consultar el gasto de sueldos para un empleado")
                    print("x) Para salir")
                    opcion = input("Ingrese opcion: ")
                    os.system("cls") 
                    if opcion == '1':
                        dni = input("Ingrese el dni del empleado: ")
                        try:
                            int(dni)
                        except ValueError:
                            print("El dni debe ser un numero entero")
                        else:
                            s = ITesorero(self.__arreglo).gastosSueldoPorEmpleado(dni)
                            if s == None:
                                print("DNI no encontrado")
                            else: print('El gasto para el dni {} es: {}'.format(dni,s))
                    elif opcion == 'x':
                        salir = bool('x'== opcion)
                    else:
                        print("Opcion incorrecta")
            else:
                print("Contraseña incorrecta")
        else:
            print("Ususario incorrecto")


    