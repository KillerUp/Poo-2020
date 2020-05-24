import os
from claseMenu import Menu


if __name__ == "__main__":
    
    menu = Menu()
    print("Datos cargados correctamente")

    salir = False

    while not salir:
        
        print("1) Insertar un vehiculo en una posicion.")
        print("2) Agregar un vehiulo.")
        print("3) Mostrar el tipo de vehiculo, dada una posicion.")
        print("4) Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta")
        print("5) Mostrar datos del vehiculo mas economico")
        print("6) Mostrar para todos los vehiculos: modelo, cantidad de puertas e importe de venta.")
        print("7) Guardar datos en archivo")
        print("x) Salir.")

        op= input("Ingrese opcion >> ")

        os.system("cls") 

        menu.funcion(op)

        salir = bool('x'== op)
        os.system('pause')
        os.system("cls") 