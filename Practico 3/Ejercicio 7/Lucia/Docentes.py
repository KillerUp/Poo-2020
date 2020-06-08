from Agentes import Agentes

class Docentes(Agentes):
    __carrera = ''
    __cargo = ''
    __catedra = ''

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra):
        Agentes.__init__(self,cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__= dict(
                cuil = self._Agentes__cuil,
                apellido = self._Agentes__apellido,
                nombre = self._Agentes__nombre,
                sueldoBasico = self._Agentes__sueldoBasico,
                antiguedad = self._Agentes__antiguedad,
                carrera = self.__carrera,
                cargo = self.__cargo,
                catedra = self.__catedra
                )
                )
        return d

    def calcularSueldo(self):
        sueldo = self._Agentes__sueldoBasico + ((self._Agentes__sueldoBasico * self._Agentes__antiguedad) / 100)
        if self.__cargo.lower() == 'simple':
            sueldo+= (self._Agentes__sueldoBasico * 10) / 100
        if self.__cargo.lower() == 'semiexclusivo':
            sueldo+= (self._Agentes__sueldoBasico * 20) / 100
        if self.__cargo.lower() == 'exclusivo':
            sueldo+= (self._Agentes__sueldoBasico * 50) / 100
        return sueldo

    def __str__(self):
        return '----------------------- \n Nombre: {} \n Apellido: {} \n Tipo: {} \n Sueldo: {} \n ----------------------- \n'.format(self._Agentes__nombre,self._Agentes__apellido,'Docente',self.calcularSueldo())