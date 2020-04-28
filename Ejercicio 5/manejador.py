from Alumno import alumno
import csv
class m:

    __lista = []

    def __init__(self):
        self.__lista = []

    def agrega(self,alum):
        self.__lista.append(alum)

    def carga(self):
        archivo = open('Ejercicio 5/Datos.csv')
        reader = csv.reader (archivo, delimiter = ';')
        for linea in reader:
            nombre = linea[0]
            año = linea[1]
            div = linea[2]
            inasis = linea[3]
            unalum = alumno(nombre,año,div,inasis)
            self.agrega(unalum)

    def porcent_alum(self,an,div):
        for i in self.__lista:
            anio = i.getanio()
            divi = i.getdiv()
            inasis = i.getinasis()
            if (anio == an) and (divi == div) and (inasis > alumno.getmax_inasis()):
                print('{:<25}{}%'.format(i.getnombre(),i.porcen_inasis()))