from claseVehiculo import Vehiculo


class Nuevo(Vehiculo):
    marca = 'VolksWagen'
    __version = ''

    def __init__(self, modelo, puertas, color, precio, version):
        super().__init__(modelo, puertas, color, precio)
        self.__version = str(version).lower()

    def calcularImporte(self):
        importe = self._Vehiculo__precio + ((10 * self._Vehiculo__precio) / 100)
        if self.__version == 'full':
            importe += (2 * self._Vehiculo__precio) / 100
        
        return importe
    
    def aJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                modelo = self._Vehiculo__modelo,
                puertas = self._Vehiculo__puertas,
                color = self._Vehiculo__color,
                precio = self._Vehiculo__precio,
                version = self.__version
            )
        )
        return d

    def __str__(self):
        return 'Modelo: {}\nCantidad de puertas: {}\nColor: {}\nPrecio base: {}\nMarca: {}\nVersion: {}\nPrecio de venta: {}'.format(
            self._Vehiculo__modelo,
            self._Vehiculo__puertas,
            self._Vehiculo__color,
            self._Vehiculo__precio,
            self.__marca,
            self.__version,
            self.calcularImporte()
        )