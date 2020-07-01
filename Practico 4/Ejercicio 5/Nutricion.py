
class Nutricionista(object):
    def __init__(self):
        self.__imc = None

    def calcula(self,peso,estatura):
        metros = float(estatura)/100
        cadena = ''

        self.__imc = round(float(int(peso) / (metros **2)), 2)

        if self.__imc <= 18.5:
            cadena = 'Peso inferior al normal'

        if self.__imc >= 18.5 and self.__imc <= 24.9:
            cadena = 'Peso normal'

        if self.__imc >= 25.0 and self.__imc <= 29.9:
            cadena = 'Peso superior al normal'

        if self.__imc >= 30.0:
            cadena = 'Obesidad'

        return self.__imc,cadena
