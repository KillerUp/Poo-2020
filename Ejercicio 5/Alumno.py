class alumno:

    max_asist = 8
    t_clases =  32
    __nombre = ''
    __año = 0
    __div = ''
    __inasis = 0

    def __init__(self,nombre,año,div,inasis):
        self.__nombre = nombre
        self.__año = año
        self.__div = div
        self.__inasis = inasis

    def getnombre(self):
        return self.__nombre

    def getanio(self):
        return self.__año

    def getdiv(self):
        return self.__div

    def getinasis(self):
        return self.__inasis

    def porcen_inasis(self):
        return(self.__inasis*100) / alumno.gett_clases()

    @classmethod
    def gett_clases(cls):
        return cls.t_clases

    @classmethod
    def getmax_inasis(cls):
        return cls.max_inasis

    @classmethod
    def modmax_inasis(cls,n_cant):
        cls.max_inasis = n_cant
