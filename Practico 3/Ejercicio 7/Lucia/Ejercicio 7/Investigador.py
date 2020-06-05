from Agentes import Agentes

class Investigador (Agentes):
    __areaI = ''
    __tipoI = ''

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, areaI, tipoI):
        Agentes.__init__(self,cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__areaI = areaI
        self.__tipoI = tipoI

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__= dict(
                cuil = self._Agentes__cuil,
                nombre = self._Agentes__nombre,
                apellido = self._Agentes__apellido,
                sueldoBasico = self._Agentes__sueldoBasico,
                antiguedad = self._Agentes__antiguedad,
                areaI = self.__areaI,
                tipoI = self.__tipoI          
                )
                )
        return d

    def getArea(self):
        return self.__areaI
    
    def calcularSueldo(self):
        sueldo = self._Agentes__sueldoBasico + ((self._Agentes__sueldoBasico * self._Agentes__antiguedad) / 100)
        return sueldo

    def __str__(self):
        return '----------------------- \n Nombre: {} \n Apellido: {} \n Tipo: {} \n Sueldo: {} \n ----------------------- \n'.format(self._Agentes__nombre,self._Agentes__apellido,'Investigador',self.calcularSueldo())
