from claseProvincia import Provincia


class Lista(object):
    indice = 0
    __lista = []

    def __init__(self):
        self.__lista = []

    def agregarElemento(self, elemento):
        elemento.rowid = Lista.indice
        Lista.indice += 1
        self.__lista.append(elemento)

    def getLista(self):
        return self.__lista

    def obtenerIndice(self, elemento):
        bandera = False
        i=0
        while not bandera and i < len(self.__lista):
            if self.__lista[i].rowid == elemento.rowid:
                bandera=True
            else:
                i+=1
        return i


    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            datos =  [provincia.toJSON() for provincia in self.__lista]
            )
        return d
