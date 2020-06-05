from ManejadorEmpleados import ManejadorEmpleados
from InterfazGerente import IGerente

class Gerente(object):
    __switcher=None

    def __init__(self,arreglo):
        self.__switcher = {
            '1' : self.opcion1,
            '2' : self.opcion2,
            '3' : self.opcion3,
            'x' : self.salir
        }
        self.__arreglo = arreglo

    def funcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        pass

    def opcion1(self):
        dni = input("Ingrese el dni del empleado: ")
        dinero = input("ingrese el importe que desea modificar: ")
        try:
            int(dni)
            float(dinero)
        except ValueError:
            print("El dni debe ser un numero entero")
        except ValueError:
            print("El importe debe ser un numero real")
        else:
            IGerente(self.__arreglo).modificarBasicoEPlanta(dni,dinero)

    def opcion2(self):
        dni = input("Ingrese el dni del empleado: ")
        dinero = input("ingrese el importe que desea modificar: ")
        try:
            int(dni)
            float(dinero)
        except ValueError:
            print("El dni debe ser un numero entero")
        except ValueError:
            print("El importe debe ser un numero real")
        else:
            IGerente(self.__arreglo).modificarViaticoEExterno(dni,dinero)

    def opcion3(self):
        dni = input("Ingrese el dni del empleado: ")
        dinero = input("ingrese el importe que desea modificar: ")
        try:
            int(dni)
            float(dinero)
        except ValueError:
            print("El dni debe ser un numero entero")
        except ValueError:
            print("El importe debe ser un numero real")
        else:
            IGerente(self.__arreglo).modificarValorEPorHora(dni,dinero)
