from ManejadorCosechas import ManejadorLista
from ManejadorCamiones import ManejadorCamion
import validar as val
mancam = ManejadorCamion()
man_cos = ManejadorLista()
mancam.cargarlistacamion()
man_cos.cargarlistacosecha()

def opcion2():
    dia = input("Ingrese el dia\n")
    dia = int(dia)
    dia -= 1
    ban = 1
    while ban == 1:
        if val.entero("El dia",dia) == 1 and 0 < (int(dia)) < 45:
            print("%10s" % "PATENTE", "%13s" % "NOMBRE", "%10s" % "KILOS")
            for i in range(20):
                p,nom = mancam.buscar(i) 
                print("%10s" % p, "%13s" % nom, "%10s" % man_cos.get_lista().getvalor(dia,i))
                ban = 0          
        else:
            dia = input("Ingrese el dia\n")

def opcion1():
    man_cos.mostrarkilos()

def switch(respuesta):
    funcion = menu.get(respuesta, lambda: print("Opcion incorrecta"))
    funcion()

menu = {'a': opcion1 , 'b': opcion2}
if __name__ == "__main__":
    salir = False    

    while not salir:
        print("Ingrese su opcion o x para finalizar\n")
        print("\ta_Si desea ver los kilos descargados de un camion")
        print("\tb_Si desea ver los datos de cosecha de un dia\n")
        respuesta = input("Opcion:").lower()
        salir = bool(respuesta == 'x')
        switch(respuesta)
 