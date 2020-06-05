from zope.interface import Interface

class Icoleccion(Interface):
    
    def insertarElemento(posicion, elemento):
        pass
    
    def agregarElemento(elemento):
        pass

    def mostrarElemento(posicion):
        pass