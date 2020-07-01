from Lista import Lista
from Paciente import Paciente


class Repositorio(object):
    __pacientesdecoder = None #Instacia de object encoder
    __manejador = None
    
    def __init__(self, pacientesdecoder):
        self.__pacientesdecoder = pacientesdecoder
        self.__manejador = self.__pacientesdecoder.decoder(self.__pacientesdecoder.leer())

    def valores(self, paciente):
        return paciente.getNombre(), paciente.getApellido(), paciente.getTelefono(), paciente.getAltura(), paciente.getPeso()

    def obtenerListaPacientes(self):
        return self.__manejador.getLista()

    def agregarPaciente(self, paciente):
        self.__manejador.agregarElemento(paciente)
        return paciente

    def modificarPaciente(self, paciente):
        self.__manejador.actualizar(paciente)
        return paciente

    def borrarPaciente(self, paciente):
        self.__manejador.borrarElemento(paciente)

    def grabarDatos(self):
        self.__pacientesdecoder.guardar(self.__manejador.toJSON())
