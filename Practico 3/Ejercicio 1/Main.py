from ManejaLibro import ManejaLibro
ml = ManejaLibro()
ml.cargaLibros()

def opcion1():
    idlib = int(input("Ingrese el id >> "))
    print(ml.buscarId(idlib))

def opcion2():
    pal = input("Ingrese la palabra >> ")
    ml.buscarPalabra(pal.lower())

def switch(op):
    funcion = menu.get(opcion, lambda: print("Opcion incorrecta"))
    funcion()

menu = {
    '1': opcion1,
    '2' : opcion2
}

if __name__ == "__main__":

    salir = False
    
    while not salir:
        print("1) Si desea buscar por id de libro.")
        print("2) Si desea buscar por palabra.")
        print("x) para salir.")

        opcion = input("Ingrese opcion >> ")  

        switch(opcion)
        salir = bool('x'== opcion)  