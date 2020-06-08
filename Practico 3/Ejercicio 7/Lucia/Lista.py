from Nodo import Nodo
from Agentes import Agentes
from Docentes import Docentes
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
from PersonalApoyo import PersonalApoyo
from Interface import Icoleccion
from zope.interface import implementer

@implementer(Icoleccion)

class Lista(object):
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0


    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def agregarElemento(self,elemento):
            nodo = Nodo(elemento)
            nodo.NodoSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__actual = nodo
            self.__tope += 1


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getAgente()
            self.__actual =self.__actual.getSiguiente()
            return dato
    
    def toJSON(self):
        agentes = []
        for agente in self:
            agentes.append(agente.toJSON())

        d = dict(__class__ = self.__class__.__name__, datos = agentes)
        return d

    def insertarElemento(self,posicion,elemento):
        try:
            int(posicion)
        except ValueError:
            raise Exception('La posicion debe ser un valor entero.')
        else:
            posicion = int(posicion) - 1

        if posicion < 0 or posicion > self.__tope:
            raise Exception('Indice fuera de rango.')
        else:
            if posicion == 0:
                self.agregarElemento(elemento)
            else:
                aux = self.__comienzo
                nodo = Nodo(elemento)
                i = 0
                while i < posicion and aux != None:
                    anterior = aux
                    aux = aux.getSiguiente()
                    i +=1
                if i > posicion:
                    print("No se encontro posicion")
                else:
                    nodo.NodoSiguiente(aux)
                    anterior.NodoSiguiente(nodo)
                    self.__tope += 1

    def mostrarElemento(self,posicion):
        try:
            int(posicion)
        except ValueError:
            raise Exception('La posicion debe ser un valor entero.')
        else:
            posicion = int(posicion) - 1

        if posicion < 0 or posicion > self.__tope:
            raise Exception('Indice fuera de rango.')
        else:
            if posicion == 0:
                agente = self.__comienzo.getAgente()
            else: 
                aux = self.__comienzo
                i = 0
                while i < posicion and aux != None:
                    anterior = aux
                    aux = aux.getSiguiente()
                    i+=1
                if i > posicion:
                    print("No se encontro la posicion")
                else:
                    agente = anterior.getAgente()

            if isinstance(agente,DocenteInvestigador):
                return "El Agente que se encuentra en la posicion {} es Docente Investigador".format(posicion + 1)

            if isinstance(agente,Docentes):
                return "El Agente que se encuentra en la posicion {} es Docente".format(posicion + 1)

            if isinstance(agente,Investigador):
                return "El Agente que se encuentra en la posicion {} es Investigador".format(posicion + 1)

            if isinstance(agente,PersonalApoyo):
                return "El Agente que se encuentra en la posicion {} es Personal de Apoyo".format(posicion + 1)
            
    def generaListado(self,carrera):
        lista = []
        for agente in self:
            if isinstance(agente,DocenteInvestigador):
                if agente.getCarrera().lower() == carrera.lower():
                    lista.append(agente)
        return lista

    def cantidad(self,areaI):
        conDocenteI = 0
        contInvestigador = 0
        for agente in self:
            if isinstance(agente,DocenteInvestigador):
                if agente.getArea().lower() == areaI.lower():
                    conDocenteI += 1
            if isinstance(agente,Investigador):
                if agente.getArea().lower() == areaI.lower():
                    contInvestigador += 1
        return conDocenteI,contInvestigador

    def ordenar(self):
        cambio = True
        self.__actual = self.__comienzo
        anterior = None
        siguiente = self.__comienzo.getSiguiente()
        while cambio:
            cambio = False
            while siguiente != None:
                if self.__actual.getAgente() > siguiente.getAgente():
                    cambio = True
                    if anterior != None:
                        aux = siguiente.getSiguiente()
                        anterior.NodoSiguiente(siguiente)
                        siguiente.NodoSiguiente(self.__actual)
                        self.__actual.NodoSiguiente(aux)
                    else:
                        aux = siguiente.getSiguiente()
                        self.__comienzo = siguiente
                        siguiente.NodoSiguiente(self.__actual)
                        self.__actual.NodoSiguiente(aux)
                    anterior = siguiente
                    siguiente = self.__actual.getSiguiente()
                else:
                    anterior = self.__actual;
                    self.__actual = siguiente
                    siguiente = siguiente.getSiguiente()
            self.__actual = self.__comienzo
            anterior = None
            siguiente = self.__comienzo.getSiguiente()
                    

    def listaytotal(self,categoria):
        lista = []
        total = 0
        for agente in self:
            if isinstance(agente,DocenteInvestigador):
                if agente.getCategoria() == categoria:
                    cadena = '----- \n Apellido: {} \n Nombre: {} \n Importe Extra: {} \n ----- \n'.format(agente.getApellido(),agente.getNombre(),agente.getImporte())
                    lista.append(cadena)
                    total += agente.getImporte()
        return lista,total



    



