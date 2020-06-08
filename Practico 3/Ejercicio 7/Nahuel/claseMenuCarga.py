from claseApoyo import Apoyo
from claseDocente import Docente
from claseDocenteInvestigador import DocenteInvestigador
from claseInvestigador import Investigador


class MenuCarga:
    __switcher=None
    def __init__(self):
        self.__switcher = {
            '1' : self.opcion1, #Docente
            '2' : self.opcion2, #Personal de apoyo
            '3' : self.opcion3, #Investigador
            '4' : self.opcion4, #Docente investigador
            'x' : self.salir
        }
    def funcion(self, op, dicc):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        obj = func(dicc)

        return obj
    def salir(self):
        print("Fin del prograrma.")

    def opcion1(self, dicc, docinv=False):
        
        dicc["carrera"] = input("Ingrese una carrera: ")
        dicc["cargo"] = input("Ingrese el cargo: ")
        dicc["catedra"] = input("Ingrese la catedra: ")

        if not docinv: #Si no se esta instanciando un docente investigador retorna una instancia de Docente
            return Docente(**dicc)
    
    def opcion2(self, dicc):
        dicc["categoria"] = input("Ingrese la categoria: ")
        return Apoyo(**dicc)
    
    def opcion3(self, dicc, docinv = False):
        dicc["area"] = input("Ingrese el area: ")
        dicc["tipo"] = input("Ingrese el tipo de investigacion: ")
        
        if not docinv: #Si no se esta instanciando un docente investigador retorna una instancia de Investigador
            return Investigador(**dicc)

    def opcion4(self, dicc):
        self.opcion1(dicc, True)
        self.opcion3(dicc, True)

        dicc["categoria_incentivo"] = input("Ingrese la categoria en el programa de incentivos: ")
        dicc["extra"] = input("Ingrese el importe extra: ")

        return DocenteInvestigador(**dicc)
