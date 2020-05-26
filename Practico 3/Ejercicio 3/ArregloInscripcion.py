import numpy as np
import csv
from ClaseInscripcion import Inscripcion

class ArregloInscripcion:

    __dimension = 0
    __cantidad = 0
    
    def __init__(self):
        self.__arreglo = np.empty(self.__dimension, dtype = Inscripcion)

    def cargar(self,inscripcion):
        if self.__cantidad == self.__dimension:
            self.__dimension+=1
            self.__arreglo.resize(self.__dimension)
            self.__arreglo[self.__cantidad] = inscripcion
            self.__cantidad += 1

    def retornaNyM(self,dni):
        i = 0
        ban = True
        while i <= self.__dimension and ban == True:
            if self.__arreglo[i].getDni() == dni:
                nombre, monto = self.__arreglo[i].getDatos()
                if self.__arreglo[i].getPago() != False:
                    monto = "No adeuda monto"
                ban = False
            else:
                i+=1
        return (nombre,monto)


    def listar(self, id_taller):
        print('NOMBRE     DNI     DIRECCION')
        for i in range(self.__dimension):
            if self.__arreglo[i].getID_taller() == id_taller:
                nombre,dni,direccion = self.__arreglo[i].getPersona()
                print('{}     {}     {}'.format(nombre,dni,direccion))

    def abonar(self,dni):
        i = 0
        ban = True
        while i <= self.__dimension and ban == True:
            if self.__arreglo[i].getDni() == dni:
                self.__arreglo[i].pagar()
                ban = False
            else:
                i+=1

    def datos(self):
        archivo = open("Inscripciones.csv","a+")
        for i in range (self.__dimension):
            dni = str(self.__arreglo[i].getDni())
            id_taller = str(self.__arreglo[i].getID_taller())
            fecha = str(self.__arreglo[i].getFecha())
            pago = str(self.__arreglo[i].getPago())
            archivo.write(dni)
            archivo.write(";")
            archivo.write(id_taller)
            archivo.write(";")
            archivo.write(fecha)
            archivo.write(";")
            archivo.write(pago)
            archivo.write("\n")

        archivo.close()


