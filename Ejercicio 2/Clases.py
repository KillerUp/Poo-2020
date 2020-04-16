class ViajeroFrecuente:

    __numviaj = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millasacum = 0

    def __init__(self, numviaj, dni, nombre, apellido, millasacum):
        try:
            numviaj = int(numviaj)
        except:
            print("No se pudo leer el numero de viajero")
            print("NUMERO DE VIAJERO\t", numviaj)
            pass
        else:
            self.__numviaj = numviaj

        if not dni.isnumeric():
            print("ERROR: El DNI no puede contener letras y/o caracteres especiales")
            print("DNI\t", dni)
            pass
        else:
            self.__dni = dni

        for char in nombre:
            if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
                print("ERROR: El nombre no puede contener numeros y/o caracteres especiales")
                print("NOMBRE\t", nombre)
                break
            pass
        else:
            self.__nombre = nombre

        for char in apellido:
            if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
                print("ERROR: El el apellido no puede contener numeros y/o caracteres especiales")
                print("APELLIDO\t", apellido)
                pass
        else:
            self.__apellido = apellido
        
        try:
            millasacum = int(millasacum)
        except:
            print("No se pudo leer las millas acumuladas")
            print("MILLAS ACUMULADAS\t", millasacum)
            pass
        else:
            self.__millasacum = millasacum
            pass

    def cantidadTotaldeMillas(self):
        return(self.__millasacum)
    
    def acumularMillas(self, millas = 0):
        self.__millasacum += millas
        pass

    def canjearMillas(self, millas = 0):
        if(millas > self.__millasacum):
            print("ERROR: el viajero no posee suficientes millas acumuladas")
            return(-1)
        else:
            self.__millasacum -= millas

        pass
    
    def esViajero(self, num = 0):
        if self.__numviaj == num:
            return 1
        else:
            return 0

    def mostrardatos(self):
        print(self.__numviaj, self.__dni, self.__nombre, self.__apellido, self.__millasacum)
    pass