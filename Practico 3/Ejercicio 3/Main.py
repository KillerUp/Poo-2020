import os
from claseMenu import Menu


if __name__ == "__main__":
    menu = Menu()
    print("Datos cargados correctamente")

    salir = False

    while not salir:
        
        print("1) Inscribir una persona en un taller.")
        print("2) Consultar inscripcion.")
        print("3) Consultar inscriptos")
        print("4) Registrar pago.")
        print("5) Guardar inscripciones")
        print("x) Salir.")

        op= input("Ingrese opcion >> ")

        os.system("cls") 

        menu.funcion(op)

        salir = bool('x'== op)
        os.system('pause')
        os.system("cls") 