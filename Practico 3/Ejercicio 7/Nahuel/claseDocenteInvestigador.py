from claseDocente import Docente
from claseInvestigador import Investigador


class DocenteInvestigador(Docente, Investigador):
    __categiria_incentivo = ''
    __extra = 0.0

    def __init__(self, categoria_incentivo, extra, **claves):
        super().__init__(**claves)
        try:
            self. __extra = float(extra)
        except:
            raise Exception("El importe extra debe ser un valor entero o real.")
        self.__categiria_incentivo = categoria_incentivo
    
    def getExtra(self):
        return self.__extra

    def toJSON(self):
        diccionario = super().toJSON()
        
        diccionario["__atributos__"].update(dict(
            categoria_incentivo = self.__categiria_incentivo,
            extra = self.__extra
        ))

        return diccionario

    def calcularSueldo(self):
        return super().calcularSueldo() + self.__extra

    def __lt__(self, otro):
        return self.getNombre > otro.getNombre

    def __str__(self):
        cadena = super().__str__()
        cadena += "Categoria de incentivo: {}\nExtra: {}\n".format(
            self.__categiria_incentivo,
            self.__extra
        )
        return cadena