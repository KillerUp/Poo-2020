from zope.interface import Interface

class IColeccion(Interface):
    
    def insertarElemento(posicion, elemento):
        pass
    
    def agregarElemento(elemento):
        pass

    def mostrarElemento(posicion):
        pass