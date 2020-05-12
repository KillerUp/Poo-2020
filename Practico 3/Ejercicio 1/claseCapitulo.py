class Capitulo(object):
    __titulo = ''
    __cantidadPaginas = 0

    def __init__(self,titulo,cant):
        self.__titulo = titulo
        self.__cantidadPaginas = int(cant)

    def getTitulo(self):
        return self.__titulo

    def getPaginas (self):
        return self.__cantidadPaginas