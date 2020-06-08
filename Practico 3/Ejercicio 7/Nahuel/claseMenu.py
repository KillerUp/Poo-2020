from claseLista import Lista
from claseMenuCarga import MenuCarga
from objectEncoder import objetEncoder


class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = {
            '1' : self.opcion1,
            '2' : self.opcion2,
            '3' : self.opcion3,
            '4' : self.opcion4,
            '5' : self.opcion5,
            '6' : self.opcion6,
            '8' : self.opcion8,
            'x' : self.salir
        }
        self.__lista = Lista()
        self.menu_de_carga = MenuCarga()
        self.__enc = objetEncoder()
        self.__lista = self.__enc.decodificar(self.__enc.leerJSON('personal.json'))
    def funcion(self, op):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print("Fin del prograrma.")

    def opcion1(self):
        obj = {}

        obj["cuil"] = input("Ingrese el CUIL (XX-XXXXXXX-X): ")
        obj["apellido"] = input("Ingrese el apellido: ")
        obj["nombre"] = input("Ingrese el nombre: ")
        obj["sueldo"] = input("Ingrese el sueldo: ")
        obj["antiguedad"] = input("Ingrese la antiguedad: ")

        print(
            '''La persona es:
            \t1)Docente.\n
            \t2)Personal de apyo.\n
            \t3)Investigador\n
            \t4)Docente Investigador\n\n'''
        )

        opt = input("Ingrese una opcion: ")

        personal = self.menu_de_carga.funcion(opt, obj)

        posicion = input("Ingrese la posicion: ")

        self.__lista.insertarElemento(posicion, obj)

    def opcion2(self):
        obj = {}

        obj["cuil"] = input("Ingrese el CUIL (XX-XXXXXXX-X): ")
        obj["apellido"] = input("Ingrese el apellido: ")
        obj["nombre"] = input("Ingrese el nombre: ")
        obj["sueldo"] = input("Ingrese el sueldo: ")
        obj["antiguedad"] = input("Ingrese la antiguedad: ")

        print(
            '''La persona es:
            \t1)Docente.\n
            \t2)Personal de apyo.\n
            \t3)Investigador\n
            \t4)Docente Investigador\n\n'''
        )

        opt = input("Ingrese una opcion: ")

        personal = self.menu_de_carga.funcion(opt, obj)

        self.__lista.agregarElemento(personal)

    def opcion3(self):
        posicion = input("Ingrese una posicion: ")

        print("Objeto almacenado en la posicion {}: {}".format(posicion, self.__lista.mostrarElemento(posicion)))
    
    def opcion4(self):
        docentes_investigadores = []
        carrera = input("Ingrese una carrera: ").lower()
        for personal in self.__lista:
            if type(personal).__name__ == "DocenteInvestigador":
                if personal.getCarrera().lower() == carrera:
                    docentes_investigadores.append(personal)
        docentes_investigadores.sort()

        for docente in docentes_investigadores:
            print(docente)

    def opcion5(self):
        area = input("Ingrese un area de investigacion: ")
        docentes_investigadores = 0
        investigadores = 0

        for personal in self.__lista:
            if type(personal).__name__ in ['Investigador', 'DocenteInvestigador']:
                if personal.getArea().lower() == area.lower():
                    if type(personal).__name__  == 'DocenteInvestigador':
                        docentes_investigadores += 1
                    else:
                        investigadores += 1
        print("Personal en el area:\n\tDocentes investigadores: {}\n\tInvestigadores: {}".format(docentes_investigadores, investigadores))

    def opcion6(self):
        for personal in self.__lista:
            print(personal)

    def opcion7(self):
        categoria = input("Ingrese una categoria")
        lista_doecntes = []
        importe_extra = 0

        for personal in self.__lista:
            if type(personal).__name__ == 'DocenteInvestigador':
                if personal.getTipo() == categoria.upper():
                    lista_doecntes.append(personal)

        if not lista_doecntes:
            print("No se encontro personal en esta categoria")
        else:
            for docente in lista_doecntes:
                print("Nombre: {}\nApellido: {}\nImporte extra: {}".format(docente.getNombre(), docente.getApellido(), docente.getExtra()))
                importe_extra += docente.getExtra()
            print("Import total:", importe_extra)

    def opcion8(self):
        dicc = dict(
            personal = [persona.aJSON() for persona in self.__lista]
            )
        self.__enc.guardarJSON('personal.json', dicc)