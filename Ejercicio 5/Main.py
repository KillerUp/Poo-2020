from manejador import m
from Alumno import alumno
ma = m()
ma.carga()

def opcion1():
    anio = input('Ingrese un año: ')
    div = input('Ingrese una division (A, B, C, D): ').upper()
    print('{:25}{}'.format('Alumno','Porcentaje') + '\n')
    ma.porcent_alum(anio, div) 

def opcion2():
    cant = int(input('Ingrese la nueva cantidad de inasistencias permitidas: '))
    alumno.modmax_inasis(cant)

menu = {
    'a': opcion1,
    'b': opcion2
    }
def switch(opt):
    fun = menu.get(opt, lambda: print('Opcion incorrecta'))
    fun()
    

if __name__ == "__main__":

    salir = False

    while not salir:
        print('a) Mostrar porcentaje de inasistencias')
        print('b) Modificar cantidad maxima de inasistencias permitidas')
        print('x) Salir')
        resp = input('Ingrese una opcion >>').lower()
       
        switch(resp)

        salir = bool('x' == resp)


    
    

    pass