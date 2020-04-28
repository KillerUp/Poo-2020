class FechaHora:
    __año = 0
    __mes = 0
    __dia = 0
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__ (self, dia = 1, mes = 1, año = 2020, hora = 0, minutos = 0, segundos = 0):
        if año > 0:
            self.__año = año
        else: 
            print("ERROR: El año no es valido") #Valida el año

        if 1 <= mes <= 12:
            self.__mes = mes #Valida el mes
        else:
            print("ERROR: mes no valido")

        if 1 <= dia <=31: #Valida el dia
            if mes == 2 and año % 400 == 0 and dia <= 29: #Valida que en febrero sea menor o igual a 28
                self.__dia = dia
            if mes == 2 and año % 400 != 0 and dia <=28: #Valida que en año bisiesto en febrero sea menor o igual a 29
                self.__dia = dia
            if (1 <= mes <= 7 and mes!=2 and mes % 2 !=0 and dia <= 31) or ( 8<= mes <=12 and mes % 2 == 0 and dia <= 31): #Valida los dias para meses que tienen 31 dias
                self.__dia = dia
            if (1 <= mes <= 7 and mes != 2 and mes % 2 == 0 and dia <= 30) or ( 8<= mes <=12 and mes % 2 != 0 and dia <= 30): #Valida los dias para meses que tienen 30 dias
                self.__dia = dia
        else:
            print("ERROR: El dia no es valido")

        if 0 <= hora <= 23:  #Valida la hora
            self.__hora = hora
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
        pass

    def __str__(self):
       return'{}/{}/{}  {} Hs {} Min {} Seg' .format(self.__dia,self.__mes,self.__año,self.__hora,self.__minutos,self.__segundos)

    def __add__(self,otra):
            a = FechaHora(self.__dia , self.__mes, self.__año, self.__hora, self.__minutos, self.__segundos)
            a.AdelantarHora(otra.get_hora(),otra.get_minutos(),otra.get_segundos())
            return a

    def __sub__(self,otro):
        a = FechaHora(self.__dia, self.__mes, self.__año, self.__hora, self.__minutos, self.__segundos)
        a.retrasarhora(otro.get_hora(), otro.get_minutos(), otro.get_segundos())
        return a

    def __gt__(self,otro):
        if(self.__año == otro.get_año()):
            if(self.__mes == otro.get_mes()):
                if(self.__dia == otro.get_dia()):
                    if(self.__hora == otro.get_hora()):
                        if(self.__minutos == otro.get_minutos()):
                            if(self.__segundos == otro.get_segundos()):
                                return False
                            else:
                                if(self.__segundos > otro.get_segundos()):
                                    return True
                                else:
                                    return False
                        else:
                            if(self.__minutos > otro.get_minutos()):
                                return True
                            else:
                                return False
                    else:
                        if(self.__hora > otro.get_hora()):
                            return True
                        else:
                            return False
                else:
                    if(self.__dia > otro.get_dia()):
                        return True
                    else:
                        return False
            else:
                if(self.__mes > otro.get_mes()):
                    return True
                else:
                    return False
        else:
            if(self.__año > otro.get_año()):
                return True
            else:
                return False


    def get_hora(self):
            return self.__hora

    def get_minutos(self):
            return self.__minutos

    def get_segundos(self):
            return self.__segundos

    def get_dia(self):
        return self.__dia

    def get_mes(self):
        return self.__mes

    def get_año(self):
        return self.__año

   
    def PonerEnHora(self, hora = 0, minutos = 0 , segundos = 0):
        self.__hora = int(hora)
        self.__minutos = int(minutos)
        self.__segundos = int(segundos)

    def AdelantarHora(self, hora = 0, minutos = 0, segundos = 0):
        self.__segundos += int(segundos)
        self.__minutos+= int(minutos)
        self.__hora += int(hora)

        if self.__segundos > 59:
            a = self.__segundos - 60
            self.__segundos = a
            self.__minutos += 1

        if self.__minutos > 59:
            a = self.__minutos - 60
            self.__minutos = a
            self.__hora += 1

        if self.__hora > 23:
            a = self.__hora - 24
            self.__hora = a
            self.__dia += 1
        
        if self.__mes == 2 and self.__año % 400 == 0 and self.__dia > 29:
            a = self.__dia - 29
            self.__dia = a
            self.__mes += 1
        if self.__mes == 2 and self.__año % 400 != 0 and self.__dia > 28:
            a = self.__dia - 28
            self.__dia = a
            self.__mes += 1
        if (1 <= self.__mes <= 7 and self.__mes!=2 and self.__mes % 2 !=0 and self.__dia > 31) or ( 8<= self.__mes <= 12 and self.__mes % 2 == 0 and self.__dia > 31):
            a = self.__dia - 31
            self.__dia = a
            self.__mes += 1
        if (1 <= self.__mes <= 7 and self.__mes != 2 and self.__mes % 2 == 0 and self.__dia > 30) or ( 8<= self.__mes <= 12 and self.__mes % 2 != 0 and self.__dia > 30):
            a = self.__dia - 30
            self.__dia = a
            self.__mes += 1

        if self.__mes > 13:
            a = self.__mes - 12
            self.__mes = a
            self.__año += 1
    

    def retrasarhora(self,hora = 0,minutos = 0,segundos = 0):
        self.__segundos -= int(segundos)
        self.__minutos-= int(minutos)
        self.__hora -= int(hora)

        if self.__segundos < 0:
            a = self.__segundos + 60
            self.__segundos = a
            self.__minutos -= 1

        if self.__minutos < 0:
            a = self.__minutos + 60
            self.__minutos = a
            self.__hora -= 1

        if self.__hora < 0:
            a = self.__hora + 24
            self.__hora = a
            self.__dia -= 1
        
        if self.__mes == 2 and self.__año % 400 == 0 and self.__dia < 1:
            a = self.__dia + 29
            self.__dia = a
            self.__mes -= 1
        if self.__mes == 2 and self.__año % 400 != 0 and self.__dia < 1:
            a = self.__dia + 28
            self.__dia = a
            self.__mes -= 1
        if (1 <= self.__mes <= 7 and self.__mes!=2 and self.__mes % 2 !=0 and self.__dia < 1) or ( 8<= self.__mes <= 12 and self.__mes % 2 == 0 and self.__dia < 1):
            a = self.__dia + 31
            self.__dia = a
            self.__mes -= 1
        if (1 <= self.__mes <= 7 and self.__mes != 2 and self.__mes % 2 == 0 and self.__dia < 1) or ( 8<= self.__mes <= 12 and self.__mes % 2 != 0 and self.__dia < 1):
            a = self.__dia + 30
            self.__dia = a
            self.__mes -= 1

        if self.__mes < 1:
            a = self.__mes + 12
            self.__mes = a
            self.__año -= 1

  
        



    