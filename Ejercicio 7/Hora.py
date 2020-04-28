class Hora:
    __h = 0
    __minutos = 0
    __segundos = 0

    def __init__(self, h = 0 ,minutos = 0 , segundos = 0):

        if 0 <= h <= 23:  #Valida la hora
            self.__h = h
        else:
            print("ERROR: La hora no es valida")

        if 0 <= minutos <= 59:    #Valida los minutos 
            self.__minutos = minutos
        else: 
            print("ERROR: Los minutos no son validos")

        if 0 <= segundos <= 59:   #valida los segundos
            self.__segundos = segundos
        else:
            print("ERROR: Los segundos no son validos")

    def get_hora(self):
            return self.__h

    def get_minutos(self):
            return self.__minutos

    def get_segundos(self):
            return self.__segundos


    def Mostrar(self):
        print('HORA: {}   MINUTOS: {}  SEGUNDOS: {}'.format(self.__h,self.__minutos,self.__segundos))


    
