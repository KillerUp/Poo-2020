from claseMenu import Menu

import os


if __name__ == "__main__":
    
    menu = Menu()
    
    salir = False

    while not salir:
        
        print("1) Insertar un vehículo en la colección en una posición determinada.")
        print("2) Agregar un vehículo a la colección.")
        print("3) Mostrar el tipo de objeto en una posicion determinada.")
        print("4) Modificar precio por patente.")
        print("5) Mostrar datos del vehiculo mas economico.")
        print("6) Mostrar para todos los vehículos que la concesionaria tiene a la venta.")
        print('7) Guardar la lista de vehiculos en el archivo "vehiculos.json."')
        print("x) Salir.")

        op= input("Ingrese opcion >> ")

        os.system("cls") 

        menu.funcion(op)

        salir = bool('x'== op)
        os.system('pause')
        os.system("cls") 