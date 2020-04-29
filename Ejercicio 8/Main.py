from Conjunto import Conjunto

def carga():
    elementos = input('Ingrese los elementos del conjunto A (SEPARADOS POR ESPACIO): ')
    a = Conjunto(elementos.split(' '))

    elementos = input('Ingrese los elementos del conjunto B (SEPARADOS POR ESPACIO): ')
    b = Conjunto(elementos.split(' '))

    print('Conjunto A =', a.getconjunto())
    print('Conjunto B = ', b.getconjunto())
    return (a,b)

def opcion1():
    a,b = carga()
    union = a + b
    print('Union del conjunto A y el conjunto B = ', union.getconjunto())

def opcion2():
    a,b = carga()
    diferencia = a - b
    print('Diferencia entre el conjunto A y el conjunto B = ', diferencia.getconjunto())

def opcion3():
    a,b = carga ()
    if a == b:
        print("El conjunto A y el conjunto B son iguales")
    else: 
        print("El conjunto A y el conjunto B son diferentes")

menu = {
    'a': opcion1,
    'b': opcion2,
    'c': opcion3
    }
def switch(opt):
    fun = menu.get(opt, lambda: print('Opcion incorrecta'))
    fun()
    
if __name__ == "__main__":
    salir = False
    while not salir:
        print('a) Si desea realizar la union de dos conjuntos')
        print('b) Si desea realizar la diferencia entre dos juntos')
        print('c) Verificar si dos conjuntos son iguales')
        print('x) Salir')
        resp = input('Ingrese una opcion >>').lower()
       
        switch(resp)

        salir = bool('x' == resp)
