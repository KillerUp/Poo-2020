import csv
import validar as val
from Camion import Camion

class ManejadorCamion(object):
    __lista = []
    def __init__(self):
        self.__lista = []
    
    def cargarlistacamion(self):
        archivo = open('Camiones.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for linea in reader:
            if val.entero("Identificador", linea[0]) and val.nombre("Nombre", linea[1]) and val.alfanum("Patente", linea[2]) and val.cadena("Marca del camion", linea[3]) and val.entero("Tara", linea[4]) ==1:
                aux = Camion((linea[0]), linea[1], linea[2], linea[3], linea[4])
                self.__lista.append(aux)
        pass
    def buscar(self,id):
        for i in range(len(self.__lista)):
            if i == id:
                a,b = self.__lista[i].getDatos()
                return(a,b)