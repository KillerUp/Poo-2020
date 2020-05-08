import csv
from Cosecha import Cosecha
import validar as val
class ManejadorLista(object):

    def __init__(self):
        self.__lista = Cosecha()

    def cargarlistacosecha(self):
        archivo = open('Cosechas.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for linea in reader:
            self.__lista.addpeso(int(linea[0])-1, int(linea[1])-1, int(linea[2]))


    def mostrarkilos(self):
        num =input("Ingrese el id\n")
        ban = 1
        acum = 0
        while ban == 1 :
            if val.entero("id camion",num) == 1 and 0 < (int(num) - 1) < 20:
                for i in range(44):
                    acum += self.__lista.getvalor(int(i),int(num) - 1)
                print("La cantidad de kilos cargados del camion", num, "es",acum)
                ban = 0
            else:
                    num = input("Ingrese el id\n")
                    num -= 1
    def get_lista(self):
        return self.__lista