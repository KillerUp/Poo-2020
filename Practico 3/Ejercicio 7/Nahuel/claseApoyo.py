from clasePersonal import Personal


class Apoyo(Personal):
    __categoria = ''

    def __init__(self, categoria, **claves):
        super().__init__(**claves)
        if not (categoria >= 1 and categoria <= 22):
            raise Exception("La categoria debe ser un numero entre 1 y 22.")
        self.__categoria = categoria 
    
    def toJSON(self):
        diccionario = super().toJSON()
        
        diccionario["__atributos__"].update(dict(
            categoria = self.__categoria
        ))
        return diccionario
    
    def calcularSueldo(self):
        sueldo_precalculado = super().calcularSueldo()

        if self.__categoria >= 1 and self.__categoria <= 10:
            porcentaje_por_categoria = 10
        elif self.__categoria > 10 and self.__categoria < 21:
            porcentaje_por_categoria = 20
        else:
            porcentaje_por_categoria = 30
        
        return sueldo_precalculado + (porcentaje_por_categoria * self.getSueldo / 100)
