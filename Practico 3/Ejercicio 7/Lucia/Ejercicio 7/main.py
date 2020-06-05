from ClaseMenu import Menu
import os

if __name__ == "__main__":
    
    menu = Menu()
    print("Datos cargados correctamente")

    salir = False

    while not salir:
        
        print("1) Insertar un agente en una posicion.")
        print("2) Agregar un agente.")
        print("3) Mostrar el tipo de agente, dada una posicion.")
        print("4) Dada una carrera, generar listado")
        print("5) Dada un area, mostrar cantidad de investigadores y de docentes investigadores")
        print("6) Mostrar listado de todos los agentes.")
        print("7) Dada una categoria, mostrar listado")
        print("8) Guardar datos en archivo")
        print("x) Salir.")

        op= input("Ingrese opcion >> ")

        os.system("cls") 

        menu.funcion(op)

        salir = bool('x'== op)
        os.system('pause')
        os.system("cls") 