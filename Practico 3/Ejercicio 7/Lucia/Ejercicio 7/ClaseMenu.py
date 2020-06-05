from Lista import Lista
from ObjectEncoder import ObjectEncoder
import json
from Docentes import Docentes
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
from PersonalApoyo import PersonalApoyo

class Menu(object):
    __switcher=None
    def __init__(self):
        self.__switcher = {
            '1' : self.opcion1,
            '2' : self.opcion2,
            '3' : self.opcion3,
            '4' : self.opcion4,
            '5' : self.opcion5,
            '6' : self.opcion6,
            '7' : self.opcion7,
            '8' : self.opcion8,
            'x' : self.salir
            }

        self.__lista = Lista()
        obj = ObjectEncoder()
        self.__lista = obj.decoder(obj.leer("Practico 3/Ejercicio 7/Personal.json"))
        

    def funcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print("Fin del prograrma.")

    def opcion1(self):
        posicion = input('Ingrese la posicion: ')
        agente = self.ingresarAgente()
        self.__lista.insertarElemento(posicion,agente)
    
    def ingresarAgente(self):
        ban = False
        tipo = None
        cuil = input("Ingrese su cuil: ")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        sueldoBase = float(input("Ingrese el sueldo base: "))
        antiguedad = int(input('Ingrese su antiguedad: '))
        while ban == False:
            tipo = input("Ingrese su roll: \n Si es docente ingrese: D \n Si es investigador ingrese: I \n Si es docente investigador ingrese: DI \n Si es personal de apoyo ingrese: PA \n")
            if tipo.upper() == 'D':
                carrera,cargo,catedra = self.un_docente()
                agente = Docentes(cuil,apellido,nombre,sueldoBase,antiguedad,carrera,cargo,catedra)
                ban = True
            if tipo.upper() == 'I':
                areaI,tipoI = self.un_investigador()   
                agente = Investigador(cuil,apellido,nombre,sueldoBase,antiguedad,areaI,tipoI)
                ban = True
            if tipo.upper() == 'DI':
                carrera,cargo,catedra = self.un_docente()
                areaI,tipoI = self.un_investigador() 
                importeExtra = float(input('Ingrese el importe: '))
                categoria = input('Ingrese categoria: ')
                agente = DocenteInvestigador(cuil,apellido,nombre,sueldoBase,antiguedad,carrera,cargo,catedra,areaI,tipoI,importeExtra,categoria)
                ban = True
            if tipo.upper() == 'PA':
                categoria = input('Ingrese su categoria (Debe ser un valor entero):')
                try:
                    int(categoria)
                except TypeError:
                    print('Error debe ser un valor entero')
                else:
                    agente = PersonalApoyo(cuil,apellido,nombre,sueldoBase,antiguedad,categoria)
                    ban = True
            if tipo.upper() != 'D' and tipo.upper() != 'I' and tipo.upper() != 'DI' and tipo.upper() != 'PA': 
                print('Opcion incorrecta \n')
                
        return agente

    def un_docente(self):
        carrera = input("Ingrese la carrera: ")
        cargo = input('Ingrese el cargo: ')
        catedra = input('Ingrese la catedra: ')
        return carrera,cargo,catedra
    
    def un_investigador(self):
        areaI = input('Ingrese su area de investigacion: ')
        tipoI = input('Ingrese el tipo de investigacion: ')
        return areaI,tipoI

    def opcion2(self):
        agente = self.ingresarAgente()
        self.__lista.agregarElemento(agente)
        
    def opcion3(self):
        p = input('Ingrese la posicion: ')
        cadena = self.__lista.mostrarElemento(p)
        print(cadena)
        
    def opcion4(self):
        carrera = input("Ingrese la carrera: ")
        listado = self.__lista.generaListado(carrera)
        listado.sort()
        for agente in listado:
            print(agente.mostrarDatos())
        
    def opcion5(self):
        areaI = input('Ingese el area de investigacion: ')
        docenteInvestigador,investigador = self.__lista.cantidad(areaI)
        print('En el area {}, hay {} Investigadores y {} Docentes Investigadores'.format(areaI,investigador,docenteInvestigador))

    def opcion6(self):
        self.__lista.ordenar()
        for agente in self.__lista:
            print(agente)

    def opcion7(self):
        categoria = input('Ingrese la categoria: ')
        lista,total = self.__lista.listaytotal(categoria)
        for i in range(len(lista)):
            print(lista[i])
        print('El total a pagar es: ',total)

    def opcion8(self):
        obj = ObjectEncoder()
        obj.guardar(self.__lista.toJSON(),'Practico 3/Ejercicio 7/Personal.json')