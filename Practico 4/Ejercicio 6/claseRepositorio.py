from Lista import Lista
from claseProvincia import Provincia


class Repositorio(object):
    __provinciasdecoder = None #Instacia de object encoder
    __manejador = None
    
    def __init__(self, provinciasdecoder):
        self.__provinciasdecoder = provinciasdecoder
        self.__manejador = self.__provinciasdecoder.decoder(self.__provinciasdecoder.leer())

    def valores(self, provincia):
        return provincia.getnombreprovincia(), provincia.getnombrecapital(), provincia.gethabitantes(), provincia.getdepartamentos()

    def obtenerListaProvincias(self):
        return self.__manejador.getLista()

    def agregarProvincia(self, provincia):
        self.__manejador.agregarElemento(provincia)
        return provincia

    def grabarDatos(self):
        self.__provinciasdecoder.guardar(self.__manejador.toJSON())
