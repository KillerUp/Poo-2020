from FechaHora import FechaHora 
from ClasePersona import Persona
from ClaseTaller import TallerCapacitacion
class Inscripcion:
    __fechaInscripcion = FechaHora()
    __pago = False
    __taller = None
    __persona = None

    def __init__(self,fecha,pago,taller,persona):
        self.__pago = pago
        aux = fecha.split('/')
        dia = int(aux[0])
        mes = int(aux[1])
        anio = int(aux[2])
        self.__fechaInscripcion = FechaHora(dia, mes, anio)
        self.__taller = taller
        self.__persona = persona

    def getDni(self):
        dni = self.__persona.getdni()
        return dni

    def getDatos(self):
        nombre = self.__taller.getNombre()
        monto = self.__taller.getMonto()
        return (nombre,monto)

    def getPago(self):
        return self.__pago

    def getID_taller(self):
        aux = self.__taller.getID()
        return aux 
    
    def getPersona(self):
        n,dni,d = self.__persona.getDatos()
        return(n,dni,d)

    def pagar(self):
        self.__pago = True

    def getFecha(self):
        return self.__fechaInscripcion



