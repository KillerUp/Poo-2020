from claseControlador import Controlador
from claseRepositorio import Repositorio
from claseVentana import VentanaPrincipal, nuevopaciente
from ObjectEncoder import ObjectEncoder

def main():
    decodificador = ObjectEncoder('Practico 4/Ejercicio 5/Pacientes.json')
    repositorio = Repositorio(decodificador)
    ventana = VentanaPrincipal()
    controlador = Controlador(repositorio, ventana)
    ventana.setcontrolador(controlador)
    controlador.comenzar()
    controlador.salirGrabarDatos()

if __name__ == "__main__":
    main()