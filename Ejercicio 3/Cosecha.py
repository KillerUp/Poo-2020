class Cosecha:
    def __init__(self):
        self.__lista = [0] * 45
        for i in range(45):
            self.__lista[i] = [0] * 20
        pass

    def addpeso(self, n = 0, m = 0, kilos = 0):
        if(0 <= n <= 45):
            self.__lista[n][m] = kilos

    def getvalor(self, i = 0, j = 0 ):
        return(self.__lista[i][j])
 
        