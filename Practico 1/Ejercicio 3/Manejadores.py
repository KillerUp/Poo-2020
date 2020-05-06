from Camion import Camion
from Cosecha import Cosecha 
from validar import entero , cadena , nombre , flotante , alfanum
import csv

def cargarlistacamion(lista):
    archivo = open('Ejercicio 3/Camiones.csv')
    reader = csv.reader(archivo, delimiter = ',')
    for linea in reader:
        if entero("Identificador", linea[0]) and nombre("Nombre", linea[1]) and alfanum("Patente", linea[2]) and cadena("Marca del camion", linea[3]) and entero("Tara", linea[4]) ==1:
            aux = Camion((linea[0]), linea[1], linea[2], linea[3], linea[4])
            lista.append(aux)
    pass

def cargarlistacosecha(cos):
    archivo = open('Ejercicio 3/Cosechas.csv')
    reader = csv.reader(archivo, delimiter = ',')
    for linea in reader:
        cos.addpeso(int(linea[0])-1, int(linea[1])-1, int(linea[2]))
    pass


def mostrarkilos(cosecha):
    num =input("Ingrese el id\n")
    ban=1
    acum = 0
    while ban == 1 :
        if entero("id camion",num) == 1 and 0 < (int(num) - 1) < 20:
            for i in range(44):
                acum += cosecha.getvalor(int(i),int(num) - 1)
            print("La cantidad de kilos cargados del camion", num, "es",acum)
            ban = 0
        else:
                num = input("Ingrese el id\n")
                num -= 1
    
        pass

def buscar(id,lista):
    for i in range(len(lista)):
        if i == id:
            a,b=lista[i].getDatos()
            return(a,b)

def mostrarlista(cosecha,lista):
    dia = input("Ingrese el dia\n")
    dia = int(dia)
    dia -= 1
    ban = 1
    while ban == 1:
        if entero("El dia",dia) == 1 and 0 < (int(dia) - 1) < 45:
            print("%10s" % "PATENTE", "%13s" % "NOMBRE", "%10s" % "KILOS")
            for i in range(20):
                p,nom = buscar(i,lista) 
                print("%10s" % p, "%13s" % nom, "%10s" % cosecha.getvalor(int(dia) - 1,i))
                ban = 0
            pass
        else:
            dia = input("Ingrese el dia\n")
            pass

        pass