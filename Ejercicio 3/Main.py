from Camion import Camion
from Cosecha import Cosecha
from Manejadores import cargarlistacamion , mostrarlista , mostrarkilos , cargarlistacosecha
import validar
import csv

if __name__ == "__main__":
    listacamion = []
    cos = Cosecha()
    cargarlistacamion(listacamion)
    cargarlistacosecha(cos)
   
    salir = False
    
    menu = {'a': mostrarkilos , 'b': mostrarlista}

    while not salir:
        print("Ingrese su opcion o x para finalizar\n")
        print("\ta_Si desea ver los kilos descargados de un camion")
        print("\tb_Si desea ver los datos de cosecha de un dia\n")
        respuesta = input("Opcion:").lower()
        salir = bool(respuesta == 'x')
        funcion = menu.get(respuesta,None)
        if funcion:
            if respuesta == 'a':
                funcion(cos)
            else: funcion(cos,listacamion)
    else:
        print("Fin del programa")
        pass

    pass