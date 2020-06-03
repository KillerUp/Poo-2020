from claseVehiculo import Vehiculo


class Usado(Vehiculo):
    __marca = ''
    __patente = ''
    __anio = 0
    __kilometraje = 0

    def __init__(self, modelo, puertas, color, precio, marca, patente, anio, kilometraje):
        super().__init__(modelo, puertas, color, precio)
        self.__marca = str(marca).capitalize()
        self.__patente = str(patente).upper()
        self.__anio = int(anio)
        self.__kilometraje = int(kilometraje)
    
    def calcularImporte(self):
        importe = self._Vehiculo__precio - (((2020 - self.__anio) * self._Vehiculo__precio) / 100)
        if self.__kilometraje > 100000:
            importe -= (2 * self._Vehiculo__precio) / 100
        return importe

    def aJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                modelo = self._Vehiculo__modelo,
                puertas = self._Vehiculo__puertas,
                color = self._Vehiculo__color,
                precio = self._Vehiculo__precio,
                marca = self.__marca,
                patente = self.__patente,
                anio = self.__anio,
                kilometraje = self.__kilometraje
            )
        )
        return d
    
    def getPatente(self):
        return self.__patente
    
    def modPrecio(self, precio):
        try:
            float(precio)
        except:
            exito = False
        else:
            self._Vehiculo__precio = float(precio)
            exito = True
        finally:
            return exito

    def __str__(self):
        return 'Modelo: {}\nCantidad de puertas: {}\nColor: {}\nPrecio base: {}\nMarca: {}\nPatente: {}\nAño: {}\nKilometraje: {}\nPrecio de venta: {}\n'.format(
            self._Vehiculo__modelo,
            self._Vehiculo__puertas,
            self._Vehiculo__color,
            self._Vehiculo__precio,
            self.__marca,
            self.__patente,
            self.__anio,
            self.__kilometraje,
            self.calcularImporte()
        )