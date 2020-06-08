from clasePersonal import Personal


class Docente(Personal):
    __carrera = ''
    __cargo = ''
    __catedra = ''
    
    def __init__(self, carrera, cargo, catedra, **claves):
        super().__init__(**claves)

        if not cargo in ['simple', 'semiexclusivo', 'exclusivo']:
            raise Exception("El cargo solo puede ser 'simple', 'semiexclusivo', 'exclusivo'")
        else:
            self.__cargo = cargo.capitalize()
        

        self.__carrera = carrera
        self.__catedra = catedra
    
    def getCarrera(self):
        return self.__carrera
    
    def toJSON(self):
        diccionario = super().toJSON()
        
        diccionario["__atributos__"].update(dict(
            carrera = self.__carrera,
            cargo = self.__cargo,
            catedra = self.__catedra
        ))

        return diccionario
    
    def calcularSueldo(self):
        sueldo_precalculado = super().calcularSueldo()

        if self.__cargo == 'simple':
            porcentaje_por_cargo = 10
        elif self.__cargo == 'semiexclusivo':
            porcentaje_por_cargo = 20
        else:
            porcentaje_por_cargo = 50
        
        return sueldo_precalculado + (porcentaje_por_cargo * self.getSueldo() / 100)


    def __str__(self):
        cadena = super().__str__()
        cadena += "Carrera: {}\nCargo: {}\nCatedra: {}\n".format(
            self.__carrera,
            self.__cargo,
            self.__catedra
        )
        return cadena