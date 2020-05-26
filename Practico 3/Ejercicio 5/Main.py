import os
from claseMenu import Menu


if __name__ == "__main__":
    
    menu = Menu()
    print("Datos cargados correctamente")

    salir = False

    while not salir:
        
        print("1) Insertar un Elemento.")
        print("2) Agregar un elemento.")
        print("3) Mostrar elementos.")
        print("x) Salir.")

        op= input("Ingrese opcion >> ")

        os.system("cls") 

        menu.funcion(op)

        salir = bool('x'== op)
        os.system('pause')
        os.system("cls") 