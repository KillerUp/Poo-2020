from Docentes import Docentes
from Investigador import Investigador
from Agentes import Agentes

class DocenteInvestigador (Docentes,Investigador):
    __importeExtra = ''
    __categoria = ''

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra,areaI,tipoI,importeExtra,categoria):
        Investigador.__init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,areaI,tipoI)
        Docentes.__init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra)
        self.__importeExtra = importeExtra
        self.__categoria = categoria

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__= dict(
                cuil = self._Agentes__cuil,
                apellido = self._Agentes__apellido,
                nombre = self._Agentes__nombre,
                sueldoBasico = self._Agentes__sueldoBasico,
                antiguedad = self._Agentes__antiguedad,
                carrera = self._Docentes__carrera,
                cargo = self._Docentes__cargo,
                catedra = self._Docentes__catedra,
                areaI = self._Investigador__areaI,
                tipoI = self._Investigador__tipoI,
                importeExtra = self.__importeExtra,
                categoria = self.__categoria         
                )
                )
        return d

    def getCarrera(self):
        return self._Docentes__carrera

    def __lt__(self, otro):
        return self._Agentes__nombre < otro._Agentes__nombre

    def mostrarDatos(self):
        cadena = '--------------- \n Cuil: {} \n Apellido: {} \n Nombre: {} \n Sueldo Basico: {}\n Antiguedad: {} \n Carrera: {} \n Cargo: {}\n Catedra: {} \n Area de Investigacion: {} \n Tipo de investigacion: {} \n Importe Extra: {} \n Categoria: {} \n --------------- \n'.format(self._Agentes__cuil,self._Agentes__apellido,self._Agentes__nombre,self._Agentes__sueldoBasico,self._Agentes__antiguedad,self._Docentes__carrera,self._Docentes__cargo,self._Docentes__catedra,self._Investigador__areaI,self._Investigador__tipoI,self.__importeExtra,self.__categoria)
        return cadena
    
    def getArea(self):
        return self._Investigador__areaI

    def calcularSueldo(self):
        sueldo = Docentes.calcularSueldo(self) + self.__importeExtra
        return sueldo

    def getCategoria(self):
        return self.__categoria

    def getApellido(self):
        return self._Agentes__apellido
    
    def getNombre(self):
        return self._Agentes__nombre

    def getImporte(self):
        return self.__importeExtra

    def __str__(self):
        return '----------------------- \n Nombre: {} \n Apellido: {} \n Tipo: {} \n Sueldo: {} \n ----------------------- \n'.format(self._Agentes__nombre,self._Agentes__apellido,'Docente Investigador',self.calcularSueldo())
    

    
    

    