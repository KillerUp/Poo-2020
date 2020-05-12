import csv

from claseSabor import Sabor


class ManejadorSabores(object):
    #Variables de instancia
    __sabores = []

    #Metodos de instancia
    def __init__(self):
        self.__sabores = []
    
    def cargaSabores(self):
        archivo_sabores = open("Practico 3/Ejercicio 2/sabores.csv")
        reader = csv.reader(archivo_sabores, delimiter = ',')

        for linea in reader:
            sabor = Sabor(*linea)
            self.__sabores.append(sabor)
    
    def buscarSabor(self, numero):
        ban = False
        i = 0
        while not ban and i < len(self.__sabores):
            if self.__sabores[i] == numero:
                ban = True
            else:
                i += 1
        
        if ban:
            return self.__sabores[i]
        else:
            return None

    def saboresMasPedidos(self):
        self.__sabores.sort()    #Ordena y retorna la lista de sabores de mayor a menor
        return self.__sabores    #y toma como criterio de ordenamiento el numero de veces pedido de cada sabor

    def __str__(self):
        cadena = ''
        for sabor in self.__sabores:
            cadena += str(sabor)
        
        return cadena