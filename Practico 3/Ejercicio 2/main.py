import os

from claseMenu import Menu


if __name__ == "__main__":
    menu = Menu()

    salir = False

    while not salir:

        print("1) Registrar un helado vendido.")
        print("2) Mostrar los 5 sabores mas vendido.")
        print("3) Estimar total de gramos vendidos para un sabor")
        print("4) Mostrar sabores vendidos por tipo de helado.")
        print("x) Salir.")

        op= input("Ingrese opcion >> ")

        os.system("cls") 

        menu.funcion(op)

        salir = bool('x'== op)
        os.system('pause')
        os.system("cls") 