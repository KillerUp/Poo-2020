from clasePersonal import Personal


class Investigador(Personal):
    __area = ''
    __tipo = ''

    def __init__(self, area, tipo, **claves):
        super().__init__(**claves)
        if not tipo.upper() in ['I','II', 'III', 'IV', 'V']:
            raise Exception("La categoria de investigacion debe ser 'I','II', 'III', 'IV' o 'V'")
        self.__tipo = tipo.upper()
        self.__area = area.lower()
        
    
    def getArea(self):
        return self.__area

    def getTipo(self):
        return self.__tipo

    def toJSON(self):
        diccionario = super().toJSON()
        
        diccionario["__atributos__"].update(dict(
            area = self.__area,
            tipo = self.__tipo
        ))

        return diccionario
    
    def __str__(self):
        cadena = super().__str__()
        cadena += "Area de investigacion: {}\nTipo de investigacion: {}\n".format(
            self.__area,
            self.__tipo
        )
        return cadena
    
    def calcularSueldo(self):
        return super().calcularSueldo()