class Provincia(object):
    __nombre_provincia = ''
    __nombre_capital = ''
    __habitantes = 0
    __departamentos = 0

    def __init__(self, nombre_provincia, nombre_capital, habitantes, departamentos):
        super().__init__()
        if not nombre_provincia.replace(' ', '').isalpha() or not nombre_capital.replace(' ', '').isalpha():
            raise ValueError('Provincia y/o capital no valida/s.')
        else:
            try:
                self.__habitantes = int(habitantes)
                self.__departamentos = int(departamentos)
            except ValueError:
                raise ValueError('La cantidad de habitantes y de departamentos debe ser un número entero mayor a cero.')
            else:
                self.__nombre_provincia = nombre_provincia
                self.__nombre_capital = nombre_capital
        if self.__habitantes < 1 or self.__departamentos < 1:
            raise ValueError('La cantidad de habitantes y de departamentos debe ser un número entero mayor a cero.')

    def getnombreprovincia(self):
        return self.__nombre_provincia
    
    def getnombrecapital(self):
        return self.__nombre_capital
    
    def gethabitantes(self):
        return self.__habitantes
    
    def getdepartamentos(self):
        return self.__departamentos

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__= dict(
                nombre_provincia = self.__nombre_provincia,
                nombre_capital = self.__nombre_capital,
                habitantes = self.__habitantes,
                departamentos = self.__departamentos
                )
                )
        return d

    def __str__(self):
        return self.__nombre_provincia.capitalize()