
class Nutricionista(object):
    def __init__(self):
        self.__IMC = None

    def calcula(self,peso,estatura):
        metros = float(estatura)/100
        self.__IMC = float(int(peso) / (metros **2))

        if self.__IMC <= 18.5:
            cadena = 'Peso inferior al normal'

        if self.__IMC >= 18.5 and self.__IMC <= 24.9:
            cadena = 'Peso normal'

        if self.__IMC >= 25.0 and self.__IMC <= 29.9:
            cadena = 'Peso superior al normal'

        if self.__IMC >= 30.0:
            cadena = 'Obesidad'

        return self.__IMC,cadena
        