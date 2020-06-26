class Fraccion(object):
    __numerador = 0
    __denominador = 0
    def __init__(self, numerador, denominador=1):
    
        try:
            self.__numerador = int(numerador)
        except:
            raise ValueError("El numerador debe ser un valor entero.")
        
        try:
            self.__denominador = int(denominador)
        except:
            raise ValueError("El denominador debe ser un valor entero.")


    def getNumerador(self):
        return self.__numerador
    
    def getDenominador(self):
        return self.__denominador

    def __add__(self, otro):
        if self.__denominador == otro.getDenominador():
            denominador = self.__denominador
        else:
            denominador = self.mcm(self.__denominador,otro.getDenominador())
        numerador = int(((denominador / self.__denominador) * self.__numerador) + ((denominador/otro.getDenominador())*otro.getNumerador()))
        cadena = '{}/{}'.format(numerador,denominador)
        return cadena

    def __sub__(self, otro):
        if self.__denominador == otro.getDenominador():
            denominador = self.__denominador
        else:
            denominador = self.mcm(self.__denominador,otro.getDenominador())
        numerador = int(((denominador / self.__denominador) * self.__numerador) - ((denominador/otro.getDenominador())*otro.getNumerador()))
        cadena = '{}/{}'.format(numerador,denominador)
        return cadena

    def __mul__(self, otro):
        numerador = self.__numerador * otro.getNumerador()
        denominador = self.__denominador * otro.getDenominador()
        cadena = '{}/{}'.format(numerador,denominador)
        return cadena
    
    def __truediv__(self, otro):
        numerador = self.__numerador * otro.getDenominador()
        denominador = self.__denominador * otro.getNumerador()
        cadena = '{}/{}'.format(numerador,denominador)
        return cadena

    def mcm(self,x, y):
        z = max(x, y)
        while True:
            if(z % x == 0) and (z % y == 0):
                return z
            else:
                z += 1
    
    def simplificar(self,valor=2):
        if self.__numerador > 0 and self.__denominador > 0:

            numerador = float(self.__numerador) / valor
            denominador = float(self.__denominador) / valor

            if numerador.is_integer() and denominador.is_integer():
                self.__numerador = numerador
                self.__denominador = denominador
                self.simplificar()
            else:        
                if(self.__numerador == valor or self.__denominador == valor or numerador <= 1 or denominador <= 1):
                    return  
                else:
                    valor += 1
                    self.simplificar(valor) 
        
        
    
    def __str__(self):
        return '{}/{}'.format(int(self.__numerador),int(self.__denominador))






    

    
