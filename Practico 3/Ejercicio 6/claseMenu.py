from claseLista import Lista
from claseNuevo import Nuevo
from claseUsado import Usado
from objetEncoder import objetEncoder
import csv
import json
import os


class Menu:
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
        self.__enc = objetEncoder()
        self.__lista = self.__enc.decodificar(self.__enc.leerJSON('vehiculos.json'))
    def funcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print("Fin del prograrma.")

    

    def opcion1(self):
        modelo = input("Ingrese el modelo: ")
        puertas = input("Ingrese la cantidad de puertas: ")
        color = input("Ingrese el color: ")
        precio = input("Ingrese el precio base: ")

        estado = input("Ingrese el estado del vehiculo (NUEVO/USADO): ").lower()

        if estado == "nuevo":
            version = input("Ingrese la version (BASE/FULL): ")
            vehiculo = Nuevo(modelo, puertas, color, precio, version)

        elif estado == "usado":
            marca = input("Ingrese la marca: ")
            patente= input("Ingrese la patente: ")
            anio = input("Ingrese el año: ")
            kilometraje = input("Ingrese el kilometraje: ")
            vehiculo = Usado(modelo, puertas, color, precio, marca, patente, anio, kilometraje)

        posicion = input("Ingrese la posicion donde desea insertar el elemento: ")

        self.__lista.insertarElemento(posicion, vehiculo)
        pass
    
    def opcion2(self):

        modelo = input("Ingrese el modelo: ")
        puertas = input("Ingrese la cantidad de puertas: ")
        color = input("Ingrese el color: ")
        precio = input("Ingrese el precio base: ")

        estado = input("Ingrese el estado del vehiculo (NUEVO/USADO): ").lower()

        if estado == "nuevo":
            version = input("Ingrese la version (BASE/FULL): ")
            vehiculo = Nuevo(modelo, puertas, color, precio, version)
            self.__lista.agregarElemento(vehiculo)

        elif estado == "usado":
            marca = input("Ingrese la marca: ")
            patente= input("Ingrese la patente: ")
            anio = input("Ingrese el año: ")
            kilometraje = input("Ingrese el kilometraje: ")
            vehiculo = Usado(modelo, puertas, color, precio, marca, patente, anio, kilometraje)
            self.__lista.agregarElemento(vehiculo)
            
    def opcion3(self):
        posicion = input("Ingrese una posicion: ")
        print(self.__lista.mostrarElemento(posicion))
        pass
    
    def opcion4(self):
        patente = input("Ingrese una patente: ")
        vehiculo = self.__lista.buscarPatente(patente)
        if vehiculo == None:
            print("Patente no encontrada.")
        else:
            precio = input("Ingrese el precio nuevo: ")
            if vehiculo.modPrecio(precio) == False:
                print("ERROR: El precio debe ser un valor entero/real")
            else:
                print("Nuevo precio de venta:", vehiculo.calcularImporte())
        pass

    def opcion5(self):
        minimo = 99999999
        vehiculo_mas_economico = None
        for vehiculo in self.__lista:
            importe = vehiculo.calcularImporte()
            if importe < minimo:
                vehiculo_mas_economico = vehiculo
                minimo = importe
        
        print(vehiculo_mas_economico)

    def opcion6(self):
        for vehiculo in self.__lista:
            print('Modelo: {}\nCantidad de puertas: {}\nPrecio de venta: {}'.format(vehiculo.getModelo(),vehiculo.getPuertas(), vehiculo.calcularImporte()))
        pass

    def opcion7(self):
        dicc = dict(
            vehiculos = [vehiculo.aJSON() for vehiculo in self.__lista]
        )
        self.__enc.guardarJSON('vehiculos.json', dicc)
        pass