from claseRepositorio import Repositorio
from claseVentana import VentanaPrincipal, nuevopaciente, VentanaIMC
from Nutricion import Nutricionista


class Controlador(object):
    def __init__(self, repositorio, ventana):
        self.repositorio = repositorio
        self.ventana = ventana
        self.seleccion = -1
        self.pacientes = list(repositorio.obtenerListaPacientes())
        self.nutricionista = Nutricionista()
    def crearPaciente(self):
        paciente = nuevopaciente(self.ventana).mostrar()
        if paciente:
            un_paciente = self.repositorio.agregarPaciente(paciente)
            self.pacientes.append(un_paciente)
            self.ventana.agregarPacientes(un_paciente)

    def seleccionarPaciente(self, indice):
        self.seleccion = indice
        paciente = self.pacientes[indice]
        self.ventana.verPaciente(paciente)

    def modificarPaciente(self):
        if self.seleccion == -1:
            return
        rowid = self.pacientes[self.seleccion].rowid
        detalles_pacientes = self.ventana.obtenerDetalles()
        detalles_pacientes.rowid = rowid
        paciente = self.repositorio.modificarPaciente(detalles_pacientes)
        self.pacientes[self.seleccion] = paciente
        self.ventana.modificarPaciente(paciente, self.seleccion)
        self.seleccion=-1

    def borrarPaciente(self):
        if self.seleccion == -1:
            return
        paciente = self.pacientes[self.seleccion]
        self.repositorio.borrarPaciente(paciente)
        self.pacientes.pop(self.seleccion)
        self.ventana.borrarPaciente(self.seleccion)
        self.seleccion=-1

    def calcularimc(self):
        paciente = self.pacientes[self.seleccion]
        imc,composicion = self.nutricionista.calcula(paciente.getPeso(), paciente.getAltura())
        ventana_imc = VentanaIMC(self.ventana, imc, composicion).mostrar()
    def comenzar(self):
        for i in self.pacientes:
            self.ventana.agregarPacientes(i)
        self.ventana.mainloop()

    def salirGrabarDatos(self):
        self.repositorio.grabarDatos()
