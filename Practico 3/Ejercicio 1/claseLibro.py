from claseCapitulo import Capitulo


class Libro(object):
    __idLibro = 0
    __titulo = ''
    __autor = ''
    __editorial = ''
    __isbn = 0
    __cantidadCapitulos = 0
    __capitulos = []

    def __init__(self, id_libro, titulo, autor, editorial, isbn, cant):
        self.__idLibro = int(id_libro)
        self.__titulo = str(titulo)
        self.__autor = str(autor)
        self.__editorial = str(editorial)
        self.__isbn = int(isbn)
        self.__cantidadCapitulos = int(cant)
        self.__lista = [] 

    def agregacap(self,titulo,cant):
        aux = Capitulo(titulo,cant)
        self.__lista.append(aux)

    def getId(self):
        return self.__idLibro

    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor

    def getCapitulos (self):
        cant_pag = 0
        titulo = ''
        cadena = ''
        for cap in self.__capitulos:
            cant_pag+= int(cap.getPaginas())
            titulo += 'Titulo: {}\n'.format(cap.getTitulo())
        cadena = titulo + 'Cantidad de paginas: {}'.format(cant_pag)
        return cadena

    def buscaPalabra(self,palabra):
        ban = False

        if palabra in self.__titulo.lower():
            ban = True
        else: 
            i = 0

            while not ban and i < len(self.__capitulos):
                if palabra in self.__capitulos[i].getTitulo().lower():
                    ban = True
                else:
                    i += 1

        return ban
