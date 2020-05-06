class Conjunto:
    def __init__(self, elem = []):
        self.__conjunto = elem
    
    def __add__(self, otro):
        union = Conjunto(list(self.__conjunto))
        for i in otro.getconjunto():
            if not i in union.getconjunto():
                union.agrega(i)
        return union
    
    def __sub__(self, otro):
        diferencia = Conjunto()
        for i in self.__conjunto:
            if not i in otro.getconjunto():
                diferencia.agrega(i)
        return diferencia
    
    def __eq__(self, otro):
        if len(self.__conjunto) == len(otro.getconjunto()):
            for i in range(len(self.__conjunto)):
                if self.__conjunto[i] != otro.getconjunto()[i]:
                    return False
            else:
                return True
        else:
            return False

    def agrega(self, num):
        self.__conjunto.append(num)

    def getconjunto(self):
        return self.__conjunto