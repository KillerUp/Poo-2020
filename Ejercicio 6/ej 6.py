from FechaHora import FechaHora

def carga():
    d=int(input("Ingrese Dia: "))
    mes=int(input("Ingrese Mes: "))
    a=int(input("Ingrese Año: "))
    h=int(input("Ingrese Hora: "))
    m=int(input("Ingrese Minutos: "))
    s=int(input("Ingrese Segundos: "))
    r = FechaHora (d,mes,a,h,m,s)
    return r


def opcion1():
    print("\nIngrese los datos del primer elemento \n")
    a = carga()
    print("\nIngrese los datos del segundo elemento \n")
    b = carga() 
    c = a+b 
    print("\nPrimer elemento:\n", a)
    print("\nSegundo elemnto: \n", b)
    print("\nSuma:\n", c)

    pass
 
def opcion2():
    print("\nIngrese los datos del primer elemento\n")
    a = carga()
    print("\nIngrese los datos del segundo elemento\n")
    b = carga()
    c = a-b 
    print("\nPrimer elemento:\n", a)
    print("\nSegundo elemnto: \n", b)
    print("\nResta: \n", c)

    pass

def opcion3():
    print("Ingrese los datos del primer elemento")
    a = carga()
    print("Ingrese los datos del segundo elemento")
    b = carga()
    print("Primer elemento:\n", a)
    print("Segundo elemnto: \n",b)
    if (a > b ):
        print("El primer elemento es mayor que el segundo elemento \n")
    else: 
        print("El primer elemento no es mayor que el segundo elemento\n")
    pass
 

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
        print('a) Sumar hora')
        print('b) Restar hora')
        print('c) Distinguir entre dos horas cuál es mayor')
        print('x) Salir')
        resp = input('Ingrese una opcion >>').lower()
       
        switch(resp)

        salir = bool('x' == resp)


    
    pass