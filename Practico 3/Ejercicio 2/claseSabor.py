class Sabor(object):
    #Variables de instancia
    __id_sabor = 0
    __nombre = ''
    __descripcion = ''
    __vecespedido = 0 #Cunta las veces que se pidio el sabor

    #Metodos de instancia
    def __init__(self, id_sabor, nombre, descripcion):
        self.__id_sabor = int(id_sabor)
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__vecespedido = 0

    def __str__(self):
        return '[{}] {}:\n\t{}\n'.format(self.__id_sabor, self.__nombre.upper(), self.__descripcion)

    def __eq__(self, numero):
        return self.__id_sabor == numero

    def __gt__(self, otro):
        return self.__vecespedido > otro.getVecesPedido() #Sobrecargo los operadores >, <, == para contar los helados mas vendidos

    def __lt__(self, otro):
        return self.__vecespedido > otro.getVecesPedido()

    def contarPedido(self):
        self.__vecespedido += 1 #incrementa el contador de pedidos

    def getVecesPedido(self):
        return self.__vecespedido
    
    def getNombre(self):
        return self.__nombre
        
    def getId(self):
        return self.__id_sabor