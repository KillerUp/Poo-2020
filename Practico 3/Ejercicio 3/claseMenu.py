from ArregloTaller import ArregloTaller
from ManejadorPersona import Manejador
from ArregloInscripcion import ArregloInscripcion
from ClasePersona import Persona
from ClaseInscripcion import Inscripcion
import os

class Menu(object):

    __switcher = None
    __ListaPersona = []
    
    def __init__(self):
        self.__switcher = {
            '1' : self.opcion1,
            '2' : self.opcion2,
            '3' : self.opcion3,
            '4' : self.opcion4,
            '5' : self.opcion5,
            'x' : self.salir
        }
        self.__ArreTaller = ArregloTaller() 
        self.__ArreTaller.carga()
        self.__ArreInscripcion = ArregloInscripcion() 
        self.__ListaPersona = []

    def funcion(self, op):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print("Fin del prograrma.")

    def opcion1(self):
        ban = False 
        fecha = input("Ingrese fecha de inscripcion:  ")
        nombre = input("Ingrese su nombre:  ")
        dni = int(input("Ingrese su dni:  "))
        direccion = input("Ingrese su direccion:  ")

        while not ban:
            id_taller = int(input("Ingrese el ID del taller al que desea inscribirse: "))
            if self.__ArreTaller.buscarporID(id_taller):
                ban = True
            else: 
                print("ERROR: ID no existe")
                os.system('pause')
        
        ban = False

        while not ban:
            nombretaller = input("Ingrese el nombre del taller al que desea inscribirse: ")
            taller = self.__ArreTaller.buscarpornombre(nombretaller)
            if taller != None:
                ban = True
            else: 
                print("ERROR: El taller no existe")
                os.system('pause')

        persona = Persona(nombre,direccion,dni)
        inscripcion = Inscripcion(fecha,False,taller,persona)
        self.__ArreInscripcion.cargar(inscripcion)
        self.__ListaPersona.append(persona)
        self.__ArreTaller.modifica(id_taller)

    def opcion2(self):
        dni = int(input("Ingrese dni: "))
        nombre,monto = self.__ArreInscripcion.retornaNyM(dni)
        print('Se inscribio en el taller: {} \n Adeuda: {}'.format(nombre,monto))

    def opcion3(self):
        ban = False
        while not ban:
            id_taller = int(input("Ingrese el ID del taller: "))
            if self.__ArreTaller.buscarporID(id_taller):
                ban = True
            else: 
                print("ERROR: ID no existe")
                os.system('pause')
            
        self.__ArreInscripcion.listar(id_taller)

    def opcion4(self):
        dni = int(input("Ingrese DNI: "))
        self.__ArreInscripcion.abonar(dni)

    def opcion5(self):
        self.__ArreInscripcion.datos()