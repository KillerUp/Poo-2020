from Nodo import Nodo
from VehiculoUsado import VehiculoUsado
from VehiculoNuevo import VehiculoNuevo
from Interface import Icoleccion
from zope.interface import implementer

@implementer(Icoleccion)

class Lista(object):
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0 

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def agregarElemento(self,elemento):
        nodo = Nodo(elemento)
        nodo.NodoSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getVehiculo()
            self.__actual =self.__actual.getSiguiente()
            return dato
    
    def toJSON(self):
        vehiculos = []
        for vehiculo in self:
            vehiculos.append(vehiculo.toJSON())

        d = dict(__class__ = self.__class__.__name__, datos = vehiculos)
        return d

    def insertarElemento(self,posicion,elemento):
        try:
            int(posicion)
        except ValueError:
            print('La posicion debe ser un valor entero.')
        else:
            posicion = int(posicion) - 1

        if posicion < 0 or posicion > self.__tope:
            raise Exception('Indice fuera de rango.')
        else:
            if posicion == 0:
                self.agregarElemento(elemento)
            else:
                aux = self.__comienzo
                nodo = Nodo(elemento)
                i = 0
                while i < posicion and aux != None:
                    anterior = aux
                    aux = aux.getSiguiente()
                    i +=1
                if i > posicion:
                    print("No se encontro posicion")
                else:
                    nodo.NodoSiguiente(aux)
                    anterior.NodoSiguiente(nodo)
                    self.__tope += 1
    
    def mostrarElemento(self,posicion):
        try:
            int(posicion)
        except ValueError:
            print('La posicion debe ser un valor entero.')
        else:
            posicion = int(posicion) - 1

        if posicion < 0 or posicion > self.__tope:
            raise Exception('Indice fuera de rango.')
        else:
            if posicion == 0:
                vehiculo = self.__comienzo.getVehiculo()
            else: 
                aux = self.__comienzo
                i = 0
                while i < posicion and aux != None:
                    anterior = aux
                    aux = aux.getSiguiente()
                    i+=1
                if i > posicion:
                    print("No se encontro la posicion")
                else:
                    vehiculo = anterior.getVehiculo()
            if isinstance(vehiculo,VehiculoNuevo):
                print("El vehiculo que se encuentra en la posicion {} es un Vehiculo Nuevo".format(posicion + 1))
            else:
                print("El vehiculo que se encuentra en la posicion {} es un Vehiculo Usado".format(posicion + 1))
    
    def ModiyMuestra(self,patente,precio):
        aux = self.__comienzo
        i = 0
        ban = False
        while i < self.__tope and aux != None and ban == False:
            vehiculo = aux.getVehiculo()
            if isinstance(vehiculo,VehiculoUsado):
                p = vehiculo.getPatente()
                if p == patente:
                    vehiculo.modificarPrecio(precio)
                    importe = vehiculo.calcularImporte()
                    ban = True
                else: 
                    i+=1
                    aux = aux.getSiguiente()
            else:
                i+=1
                aux = aux.getSiguiente()

        if i < self.__tope:
            return importe
        else:
            return None

    def menor(self):
        min = 99999999999999999
        vehiculoEconomico = None
        for vehiculo in self:
            importe = vehiculo.calcularImporte()
            if importe < min:
                min = importe
                vehiculoEconomico = vehiculo
        return vehiculoEconomico
        


        
            


