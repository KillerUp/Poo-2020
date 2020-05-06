from Clases import ViajeroFrecuente
import csv
import os

def validar(dato = '', num = '0'):
    ban = 0

    try:
        num = int(num)
    except:
        print('ERROR:', dato, 'debe ser un valor entero.')
        ban = 1
    else:
        return num

    while ban == 1:
        num = input('Ingrese un nuevo valor para ' + dato + ': ')
        try:
            num = int(num)
        except:
            print('ERROR:', dato, 'debe ser un valor entero.')
        else:
            return num

def testing():
    lista = []
    archivo = open('Ejercicio 2/Testing.csv')
    reader = csv.reader(archivo, delimiter = ',')
    for linea in reader:
        aux = ViajeroFrecuente((linea[0]), linea[1], linea[2], linea[3], linea[4])
        os.system("pause")
        os.system("cls")
        lista.append(aux)
    pass

def cargalista(lista):
    archivo = open('Ejercicio 2/Viajeros.csv')
    reader = csv.reader(archivo, delimiter = ',')
    for linea in reader:
        aux = ViajeroFrecuente((linea[0]), linea[1], linea[2], linea[3], linea[4])
        lista.append(aux)
    pass

def buscar(lista, num = 0):
    for i in range(len(lista)):
        if lista[i].esViajero(num) == 1:
            return i
    else:
        return(-1)
    pass

if __name__ == "__main__":
    lista = []
    
    #testing()
    print("Fin de la funcion testing")
    os.system("pause")
    os.system("cls")

    cargalista(lista)

    num = input("Ingrese un numero de viajero: ")
    num = validar("Numero de viajero",num)
    viajero =(buscar(lista, num))

    while( viajero == -1):
        os.system("cls")
        print("ERROR: Viajero no encontrado")
        num = int(input("Ingrese un numero de viajero: "))
        viajero = (buscar(lista, num))

    opcion = ''
    while(opcion != 'x'):

        print("\ta- Consultar cantidad de millas.")
        print("\tb- Acumular millas.")
        print("\tc- Canjear millas.")
        print("\td- Cambiar viajero")
        opcion = input("Ingrese una opcion o x para finalizar >> ")

        if opcion == 'a':
            os.system("cls")
            print("Cantidad total de millas:", lista[viajero].cantidadTotaldeMillas())
            os.system("pause")
        elif opcion == 'b':
            millas = input("Ingrese las millas del ultimo vuelo: ")
            millas = validar("Cantidad de millas", millas)
            lista[viajero].acumularMillas(millas)
        elif opcion == 'c':
            millas = input("Ingrese las cantidad de millas que desea canjear: ")
            millas = validar("Cantidad de millas", millas)
            lista[viajero].acumularMillas(millas)
        elif opcion == 'd':
            num = input("Ingrese un numero de viajero: ")
            num = validar("Numero de viajero", num)
            viajero = buscar(lista, num)

            while(viajero == -1):
                os.system("cls")
                print("ERROR: Viajero no encontrado")
                num = input("Ingrese un numero de viajero: ")
                num = validar("Numero de viajero", num)
                viajero = buscar(lista, num)
        elif opcion == 'x':
            break
        else:
            print("ERROR: Opcion invalida")
            os.system("pause")
            os.system("cls")
    pass