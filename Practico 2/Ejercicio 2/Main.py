from Manejador import Manejadorlista
from Clases import ViajeroFrecuente
import csv
import os
ml = Manejadorlista()
ml.cargalista()

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
    m = Manejadorlista()
    archivo = open('Practico 1/Ejercicio 2/Testing.csv')
    reader = csv.reader(archivo, delimiter = ',')
    for linea in reader:
        aux = ViajeroFrecuente((linea[0]), linea[1], linea[2], linea[3], linea[4])
        os.system("pause")
        os.system("cls")
        m.get_lista().append(aux)
    pass

def opcion1():
    os.system("cls")
    num = input("Ingrese un numero de viajero: ")
    num = validar("Numero de viajero",num)
    print("Cantidad total de millas:", ml.millas(num))
    os.system("pause")

def opcion2():
    num = input("Ingrese un numero de viajero: ")
    num = validar("Numero de viajero",num)
    millas = input("Ingrese las millas del ultimo vuelo: ")
    millas = validar("Cantidad de millas", millas)
    ml.acum(millas,num)

def opcion3():
    num = input("Ingrese un numero de viajero: ")
    num = validar("Numero de viajero",num)
    millas = input("Ingrese las cantidad de millas que desea canjear: ")
    millas = validar("Cantidad de millas", millas)
    ml.canj(millas,num)


def switch(opcion):
    funcion = menu.get(opcion, lambda: print('Opcion incorrecta') )
    funcion()
menu = {
    'a': opcion1,
    'b': opcion2,
    'c': opcion3
}
if __name__ == "__main__":
    
    testing()
    print("Fin de la funcion testing")
    os.system("pause")
    os.system("cls")

    salir = False

    while not salir:

        print("\ta- Consultar cantidad de millas.")
        print("\tb- Acumular millas.")
        print("\tc- Canjear millas.")
        opcion = input("Ingrese una opcion o x para finalizar >> ")
        salir = bool('x' == opcion)
        switch(opcion)

