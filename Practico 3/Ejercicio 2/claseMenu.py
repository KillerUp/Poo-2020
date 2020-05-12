import os

from claseHelado import Helado
from ManejadorHelados import ManejadorHelados
from ManejadorSabores import ManejadorSabores

class Menu(object):
    __switcher = None
    __mh = None
    __ms = None
    
    def __init__(self):
        self.__switcher = {
            '1' : self.opcion1,
            '2' : self.opcion2,
            '3' : self.opcion3,
            '4' : self.opcion4,
            'x' : self.salir
        }
        self.__mh = ManejadorHelados()
        self.__ms = ManejadorSabores()
        self.__ms.cargaSabores()

    def funcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print("Fin del prograrma.")

    def opcion1(self):
        tipos = [100, 150, 250, 500, 1000] #Lista de los valores predefinidos para validar la entrada
        sabores = [] #Listas de los sabores que se enviaran al constructor Helado

        tipo = int(input("Ingrese el tipo del helado >> "))

        while not(tipo in tipos): #Mientras el tipo ingresado no esta en la lista de valores predefinidos

            os.system('cls')
            print("ERROR: Tipo no valido.")
            tipo = int(input("Ingrese el tipo del helado >> "))

        ban = False
        while not ban: #Mientras no finalize la carga de sabores
            os.system('cls')
            print("------SELECCIONES LOS SABORES------")
            print(self.__ms) #Muestra la lista de sabores disponibles
            print("Ingrese 0 para finalizar carga de sabores\n\n")
            print("Cantidad de sabores actual: {}".format(len(sabores)))
            numero = int(input("Ingrese un numero de sabor >> "))

            if numero == 0 and len(sabores) > 0: #Si la opcion es 0 y el numero de sabores cargados es mayor que 0
                ban = True
            elif numero == 0: #Si la opcion es 0 pero el numero de helados cargados no es mayor que 0
                print("ERROR. El helado debe tener al menos 1 sabor.")
                os.system('pause')
            else:
                sabor = self.__ms.buscarSabor(numero) #Retorna el sabor encontrado o None si no lo encontro
                if sabor != None:
                    sabores.append(sabor) #Agrega el sabor encontrado a la lista de sabores del pedido
                else:
                    print("ERROR. Sabor no encontrado.")
                    os.system('pause')

        os.system('cls')

        helado = Helado(tipo, sabores) #Crea un helado con el tipo y los sabores elegidos
        self.__mh.agregarHelado(helado) #Carga el helado a la lista de helados

        print("Helado cargado correctamente")
        print(helado)

    def opcion2(self):
        
        self.__mh.contarSabores() #cuenta la cantidad de veces que se pidio cada sabor de helado
        lista_sabores = self.__ms.saboresMasPedidos()

        for i in range(5): #Muestra las 5 primeras componentes de la lista que serian los sabores mas vendidos
            print(lista_sabores[i].getNombre()) 

    def opcion3(self):
        ban = False
        while not ban:
            numero = int(input("Ingrese numero de sabor"))
            sabor = self.__ms.buscarSabor(numero) #Valida que exista el sabor
            if sabor != None:
                peso = self.__mh.pesoEstimado(numero) #Calcula el peso total estimado del sabor
                print('El total de gramos vendidos del sabor {} es: {}'.format(sabor.getNombre(),peso))
                ban = True
            else:
                print("ERROR. Sabor no encontrado.")
                os.system('pause')


    def opcion4(self):
        tipos = [100, 150, 250, 500, 1000] #Lista de los valores predefinidos para validar la entrada
        tipo = int(input("Ingrese el tipo del helado >> "))

        while not(tipo in tipos): #Mientras el tipo ingresado no esta en la lista de valores predefinidos
            os.system('cls')
            print("ERROR: Tipo no valido.") 
            tipo = int(input("Ingrese el tipo del helado >> "))

        sabores_por_tipo = self.__mh.saboresVendidos(tipo) #Lista de sabores por tipo
        print("Los sabores vendidos por el tipo {} son:".format(tipo))
        for i in range(len(sabores_por_tipo)):
            print(sabores_por_tipo[i])
        