class TallerCapacitacion:
    __IdTaller = 0
    __nombre = ''
    __vacantes = 0
    __montoInscripcion = 0

    def __init__(self,idTaller,nombre,vacante,monto):
        self.__IdTaller = int(idTaller)
        self.__nombre = nombre
        self.__vacantes = int(vacante)
        self.__montoInscripcion = int(monto)

    def getID(self):
        return self.__IdTaller
    
    def getNombre(self):
        return self.__nombre

    def modificaVacante(self):
        self.__vacantes -= 1

    def getMonto(self):
        return self.__montoInscripcion

    def __str__(self):
        cadena = 'ID: {}\nNombre: {}\nVacante: {}\nMonto: {}'.format(self.__IdTaller, self.__nombre, self.__vacantes, self.__montoInscripcion)
        return cadena
    
