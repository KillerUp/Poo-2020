from Vehiculos import Vehiculo
from datetime import date
from datetime import datetime

class VehiculoUsado(Vehiculo):
    __marca = ''
    __patente = ''
    __año = 0
    __kilometraje = 0
    
    def __init__(self, modelo, cant, color, precio,marca,patente,año,kilometraje):
        super().__init__(modelo, cant, color, precio)
        self.__marca = marca
        self.__patente = patente
        self.__año = año
        self.__kilometraje = kilometraje

    def calcularImporte(self):
        fecha = date.today()
        antiguedad = int(int(fecha.year) - self.__año)
        importeVenta = self._Vehiculo__precioBase - ((self._Vehiculo__precioBase / 100) * antiguedad)
        if self.__kilometraje > 100000:
            importeVenta += self._Vehiculo__precioBase - ((self._Vehiculo__precioBase * 2) / 100)
        return importeVenta

    def modificarPrecio(self,precio):
        self._Vehiculo__precioBase = precio

    def getPatente(self):
        return self.__patente

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__= dict(
                modelo = self._Vehiculo__modelo,
                cantidadPuertas = self._Vehiculo__cantidadPuertas,
                color = self._Vehiculo__color,
                precioBase = self._Vehiculo__precioBase,
                marca = self.__marca,
                patente = self.__patente,
                anio = self.__año,
                km = self.__kilometraje
                )
                )
        return d

    def __str__(self):
        cadena = 'Modelo: {} \n Cantidad de puertas: {} \n Color: {} \n Precio Base: {} \n Marca: {} \n Patente: {} \n Año: {} \n Kilometraje: {} \n Importe de Venta: {} \n'.format(self.getModelo(),self.getPuertas(),self.getColor(),self.getPrecio(),self.__marca,self.__patente,self.__año,self.__kilometraje,self.calcularImporte())
        return cadena

    def mostrar(self):
        cadena = '------------------------------------------------------------------ \n Modelo: {} \n Cantidad de puertas: {} \n Importe de Venta: {} \n ------------------------------------------------------------------ \n'.format(self.getModelo(),self.getPuertas(),self.calcularImporte())
        return cadena

