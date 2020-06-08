from Agentes import Agentes

class PersonalApoyo (Agentes):
    __categoria = ''

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__categoria = int(categoria)

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__= dict(
                cuil = self._Agentes__cuil,
                nombre = self._Agentes__nombre,
                apellido = self._Agentes__apellido,
                sueldoBasico = self._Agentes__sueldoBasico,
                antiguedad = self._Agentes__antiguedad,
                categoria = self.__categoria        
                )
                )
        return d
    def calcularSueldo(self):
        sueldo = self._Agentes__sueldoBasico + ((self._Agentes__sueldoBasico * self._Agentes__antiguedad) / 100)
        if self.__categoria >= 1 and self.__categoria <= 10:
            sueldo+= (self._Agentes__sueldoBasico * 10) / 100
        if self.__categoria >= 11 and self.__categoria <= 20:
            sueldo+= (self._Agentes__sueldoBasico * 20) / 100
        if self.__categoria >= 21 and self.__categoria <= 22:
            sueldo+= (self._Agentes__sueldoBasico * 30) / 100
        return sueldo

        
    def __str__(self):
        return '----------------------- \n Nombre: {} \n Apellido: {} \n Tipo: {} \n Sueldo: {} \n ----------------------- \n'.format(self._Agentes__nombre,self._Agentes__apellido,'Personal de Apollo',self.calcularSueldo())
        

        