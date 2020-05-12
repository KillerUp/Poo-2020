import csv
from claseLibro import Libro


class ManejaLibro(object):
    __libros = []

    def __init__(self):
        self.__libros = []

    def cargaLibros(self):

        archivo = open('Practico 3/Ejercicio 1/libros.csv')
        reader = csv.reader(archivo, delimiter =',')

        for linea in reader:

            if linea[0].isnumeric(): #Si la linea leida comienza con el id de un libro

                aux = Libro(*linea) #Crea una instancia de la clase Libro
                cant_cap = int(linea[5]) #Guarda la canidad de capitulos del ultimo libro leido
                
            else:

                aux.agregacap(*linea) #Agrega un capitulo a la lista de capituos del ultimo objeto libro
                cant_cap -= 1 #Descuenta el capitulo agregado de la cantidad de capitulos pendientes

                if cant_cap == 0: #Si ya no quedan mas capitulos del libro que agregar
                    
                    self.__libros.append(aux) #Agregar el libro a la lista del manejador

    def buscarId(self, id_libro):

        ban = False
        cadena = 'Libro no encontraado.'
        i = 0

        while not ban and i < len(self.__libros):
            if self.__libros[i].getId() == id_libro:
                ban = True
                cadena = 'Titulo: {}\nCapitulos: {}\n'.format(self.__libros[i].getTitulo(), self.__libros[i].getCapitulos())
            else:
                i += 1
        
        return cadena
        
                
    def buscarPalabra(self, palabra): 

        ban = False
        
        for libro in self.__libros:
            if libro.buscaPalabra(palabra):
                print('Titulo: {}\nAutor: {}\n\n'.format(libro.getTitulo(), libro.getAutor()))
        else:
            if not ban:
                print('Palabra no encontrada.')