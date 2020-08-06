from claseRepositorio import Repositorio
from claseVentana import VentanaPrincipal, nuevaprovincia
from claseClima import Clima



class Controlador(object):
    def __init__(self, repositorio, ventana):
        self.repositorio = repositorio
        self.ventana = ventana
        self.seleccion = -1
        self.provincias = list(repositorio.obtenerListaProvincias())
        self.clima = Clima()

    def crearProvincia(self):
        provincia = nuevaprovincia(self.ventana).mostrar()
        if provincia:
            una_provincia = self.repositorio.agregarProvincia(provincia)
            self.provincias.append(una_provincia)
            self.ventana.agregarprovincias(una_provincia)

    def seleccionarProvincia(self, indice):
        self.seleccion = indice
        provincia = self.provincias[indice]
        self.ventana.verprovincia(provincia,self.clima.getclima(provincia.getnombrecapital()))

  
    def comenzar(self):
        for i in self.provincias:
            self.ventana.agregarprovincias(i)
        self.ventana.mainloop()

    def salirGrabarDatos(self):
        self.repositorio.grabarDatos()
