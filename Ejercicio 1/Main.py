from Clases import Email
import os
import csv

def testing():
    cuentaPrueba = Email()
    archivo = open('Ejercicio 1/Testing.csv')
    reader = csv.reader(archivo, delimiter = ',')

    for linea in reader:
        print("Correo:", linea[0], "\nContraseña:", linea[1])
        cuentaPrueba.crearCuenta(linea[0], linea[1])
        os.system("pause")
        os.system("cls")
        pass
    pass

def cambiarcontraseña(cuenta):
    print("Modificar contraseña")

    os.system("cls")

    while(cuenta.confir_contr(input("Ingrese la contraseña actual: ")) == -1):
        print("Contraseña incorrecta!")
        os.system("pause")
        os.system("cls")
    
    cuenta.cambiar_contr(input("Ingrese la contraseña nueva: "))

    os.system("cls")

    print("Contraseña cambiada con exito\n")
    os.system("pause")
    pass

def contarDominio(dominio):
    listacuentas = []
    archivo = open('Ejercicio 1/Cuentas.csv')
    reader = csv.reader(archivo, delimiter = ',')

    for linea in reader:
        cant = len(linea)
        for i in range(cant):
            aux = Email()
            aux.crearCuenta(linea[i])
            listacuentas.append(aux)
            pass
        pass

    cant = 0

    for i in listacuentas:
        if(dominio == i.getDominio()):
            cant += 1
            pass
        pass

    return(cant)

if __name__ == "__main__":

    '''nombre = input("Ingrese su nombre: ")

    unaCuenta = Email()
    while(unaCuenta.crearCuenta(input("Ingrese un correo: "), input("Ingrese una contraseña: ")) == -1):
        os.system("pause")
        os.system("cls")
        pass

    os.system("cls")

    print("Estimado", nombre + ',', "enviaremos tus correos a la cuenta", unaCuenta.retornaEmail())

    os.system("pause")
    os.system("cls")
    
    cambiarcontraseña(unaCuenta)

    dominio = input("Ingrese un dominio: ")
    print("El dominio apareció", contarDominio(dominio), "veces")'''

    testing()
    pass