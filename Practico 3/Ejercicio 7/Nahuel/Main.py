from claseMenu import Menu

import os


if __name__ == "__main__":
    
    menu = Menu()
    
    salir = False

    while not salir:
        
        print("1) Insertar a personal a la coleccion.")
        print("2) Agregar agentes a la coleccion.")
        print("3) Mostrar que tipo de agente se encuentra en una posicion.")
        print("4) Listar docentes investigadores por carrera.")
        print("5) Contar docentes investigadores y cantidad de investigadores en un area de investigacion.")
        print("6) Listado por apellido.")
        print("7) Listado de docentes investigadores e importe extra.")
        print("8) Guardar personal en un archivo.")
        print("x) Salir.")

        op= input("Ingrese opcion >> ")

        os.system("clear") 

        menu.funcion(op)

        salir = bool('x'== op)
        input()
        os.system("clear")