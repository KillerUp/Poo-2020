from Coleccion import Lista
from ObjectEncoder import ObjectEncoder
import json
from VehiculoNuevo import VehiculoNuevo
from VehiculoUsado import VehiculoUsado
from numpy.core.defchararray import isnumeric
from Interface import Icoleccion

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
            '7' : self.opcion7,
            'x' : self.salir
            }

        self.__lista = Lista()
        obj = ObjectEncoder()
        self.__lista = obj.decoder(obj.leer("Practico 3/Ejercicio 6/Vehiculos.json"))

    def funcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print("Fin del prograrma.")

    def opcion1(self):
        vehiculo = self.ingresarVehiculo()
        p = input('Ingrese la posicion: ')
        Icoleccion(self.__lista).insertarElemento(p,vehiculo)
    
    def ingresarVehiculo(self):
        ban = False
        modelo = input("Ingrese el modelo: ")
        puertas = int(input("Ingrese cantidad de puertas: "))
        color = input("Ingrese el color: ")
        precio_base = float(input("Ingrese el precio base: "))
        while ban == False:
            tipo = input("Si es un auto nuevo ingrese: Nuevo, si es un auto usado ingrese: Usado \n")
            if tipo.lower() == 'nuevo':
                version = input("Ingrese version (Base o Full): ")
                vehiculo = VehiculoNuevo(modelo,puertas,color,precio_base,version)
                ban = True
            else:
                if tipo.lower() == 'usado':
                    marca = input("Ingrese la marca: ")
                    patente = input("Ingrese la patente: ")
                    anio = int(input("Ingrese el año: "))
                    km = int(input("Ingrese el kilometraje: "))
                    vehiculo = VehiculoUsado(modelo,puertas,color,precio_base,marca,patente,anio,km)
                    ban = True
                else: 
                    print("Ingeso mal la opcion \n")
        return vehiculo

    

    def opcion2(self):
        vehiculo = self.ingresarVehiculo()
        Icoleccion(self.__lista).agregarElemento(vehiculo)
        
    def opcion3(self):
        p = input('Ingrese la posicion: ')
        Icoleccion(self.__lista).mostrarElemento(p)
        
    def opcion4(self):
        patente = input("Ingrese su patente: ")
        precio = float(input("Ingrese el precio base que desea modificar: "))
        try:
            patente.isalnum()
            int(precio)
        except ValueError:
            print("El precio debe ser un numero") 
        except:
            print('Ingreso erroneamente su patente')
        else: 
            importe_venta = self.__lista.ModiyMuestra(patente,precio)
            if importe_venta != None:
                print('El importe de venta para la patente {} es: {}'.format(patente,importe_venta))
            else:
                print('No se enconto la patente')

    def opcion5(self):
        vehiculo = self.__lista.menor()
        print(vehiculo)

    def opcion6(self):
        for v in self.__lista:
            print(v.mostrar())

    def opcion7(self):
        obj = ObjectEncoder()
        obj.guardar(self.__lista.toJSON(),'Practico 3/Ejercicio 6/Vehiculos.json')