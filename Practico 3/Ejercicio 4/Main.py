import os
from claseMenu import Menu


if __name__ == "__main__":
    
    menu = Menu()
    print("Datos cargados correctamente")

    salir = False

    while not salir:
        
        print("1) Para registrar horas.")
        print("2) Mostrar monto total por tarea.")
        print("3) Listar empleados que reciben ayuda.")
        print("4) Mostrar sueldos.")
        print("x) Salir.")

        op= input("Ingrese opcion >> ")

        os.system("cls") 

        menu.funcion(op)

        salir = bool('x'== op)
        os.system('pause')
        os.system("cls") 