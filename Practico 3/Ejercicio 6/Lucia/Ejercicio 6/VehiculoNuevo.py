from Vehiculos import Vehiculo

class VehiculoNuevo(Vehiculo):
    __version = ''

    def __init__(self, modelo, cant, color, precio,version):
        super().__init__(modelo, cant, color, precio)
        self.__version = version
    
    def calcularImporte(self):
        importeVenta = self._Vehiculo__precioBase + ((self._Vehiculo__precioBase * 10) / 100)
        if self.__version.lower() == 'full':
            importeVenta += self._Vehiculo__precioBase + ((self._Vehiculo__precioBase * 2) / 100)
        return importeVenta

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__= dict(
                modelo = self._Vehiculo__modelo,
                cantidadPuertas = self._Vehiculo__cantidadPuertas,
                color = self._Vehiculo__color,
                precioBase = self._Vehiculo__precioBase,    
                version = self.__version            
                )
                )
        return d

    def __str__(self):
        cadena = 'Modelo: {} \n Cantidad de puertas: {} \n Color: {} \n Precio Base: {} \n Marca: {} \n  Version: {} \n Importe de Venta: {} \n'.format(self.getModelo(),self.getPuertas(),self.getColor(),self.getPrecio(),self.__marca,self.__version,self.calcularImporte())
        return cadena

    def mostrar(self):
        cadena = '------------------------------------------------------------------ \n Modelo: {} \n Cantidad de puertas: {} \n Importe de Venta: {} \n ------------------------------------------------------------------ \n'.format(self.getModelo(),self.getPuertas(),self.calcularImporte())
        return cadena
