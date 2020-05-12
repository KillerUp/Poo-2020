class Helado(object):
    #Variables de instancia
    __tipo = 0
    __sabores = []

    #Metodos de instancia
    def __init__(self, tipo, sabores):
        self.__tipo = int(tipo)
        self.__sabores = sabores
    
    def __str__(self):
        cadena = "Tipo: {}gr\n".format(self.__tipo)
        for sabor in self.__sabores:
            cadena += str(sabor)
        return cadena

    def getSabores(self):
        return self.__sabores #Retorna los sabores pedidos para un helado
    pass

    def cantidadSabores(self):
        cont = len(self.__sabores) #Retorna cuantos sabores hay por cada helado
        return cont 

    def getTipo(self): #Retorna tipo de helado
        return self.__tipo