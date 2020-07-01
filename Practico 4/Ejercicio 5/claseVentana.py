import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox, ttk

from Paciente import Paciente

#falta boton ver IMC

class ListaPacientes(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master=master)
        self.lista = tk.Listbox(self, **kw)
        scroll = tk.Scrollbar(self, command=self.lista.yview)
        self.lista.config(yscrollcommand=scroll.set)
        self.lista.pack(side=tk.LEFT, fill=tk.Y)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
    
    def insertar(self, paciente, indice=tk.END):
        self.lista.insert(indice, paciente)
    
    def borrar(self, indice):
        self.lista.delete(indice, indice)

    def modificar(self, paciente, indice):
        self.borrar(indice)
        self.insertar(paciente, indice)
    
    def binddc(self, callback):
        manejador = lambda _: callback(self.lista.curselection()[0])
        self.lista.bind("<Double-Button-1>", manejador)

class FormularioPaciente(tk.LabelFrame):
    campos = ('Nombre', 'Apellido', 'Telefono', 'Altura', 'Peso')
    def __init__(self, master=None, **kw):
        super().__init__(master=master, text="Paciente", padx=10, pady=10,  **kw)
        self.frame = tk.Frame(self)
        self.entradas = list(map(self.crearcampo, enumerate(self.campos)))
        self.frame.pack()

    def crearcampo(self, campo):
        posicion, texto = campo
        lbl_texto = tk.Label(self.frame, text=texto)
        ent_entrada = tk.Entry(self.frame, width=30)
        lbl_texto.grid(row=posicion, column=0, pady=5)
        ent_entrada.grid(row=posicion, column=1, pady=5)
        return ent_entrada
    
    def mostrarpaciente(self, paciente):
        valores = (paciente.getNombre(), paciente.getApellido(), paciente.getTelefono(), paciente.getAltura(), paciente.getPeso())
        for entrada, valor in zip(self.entradas, valores):
            entrada.delete(0, tk.END)
            entrada.insert(0, valor)
    
    def crearpaciente(self):
        valores = [entrada.get() for entrada in self.entradas]
        paciente = None
        try:
            paciente = Paciente(*valores)
        except ValueError as e:
            messagebox.showerror("Valores no validos", str(e), parent=self)
        
        return paciente

    def limpiar(self):
        for entrada in self.entradas:
            entrada.delete(0, tk.END)

class nuevopaciente(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.paciente = None
        self.formulario = FormularioPaciente(self)
        self.btn_confirmar = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.formulario.pack()
        self.btn_confirmar.pack()

    def confirmar(self):
        self.paciente = self.formulario.crearpaciente()
        if self.paciente:
            self.destroy()
    
    def mostrar(self):
        self.grab_set()
        self.wait_window()
        return self.paciente

class FrameIMC(tk.Frame):
    def __init__(self, master=None, imc=0, composicon=0, **kw):
        super().__init__(master=master, **kw)
        lbl_imc = tk.Label(self, text='IMC:', font=('Calibri', 15)).grid(row=0, column=0, sticky='W',padx=25,pady=25)
        lbl_valor_imc = tk.Label(self, text=imc, font=('Calibri', 15),bg='White',relief= 'sunken',width='25').grid(row=0, column=1, sticky='W',padx=25,pady=25)
        lbl_composicion= tk.Label(self, text='Composicion:', font=('Calibri', 15)).grid(row=1, column=0, sticky='W',padx=25,pady=25)
        lbl_valor_composicion = tk.Label(self, text=composicon, font=('Calibri', 15),bg='White',relief= 'sunken',width='25').grid(row=1, column=1, sticky='W',padx=25,pady=25)


class VentanaIMC(tk.Toplevel):
    def __init__(self, master=None, imc=0, composicion=0,**kw):
        super().__init__(master=master, **kw)
        frame = FrameIMC(self, imc, composicion, height='400',width='250')
        frame.pack()

    def mostrar(self):
        self.grab_set()
        self.wait_window()

class ActualizarPaciente(FormularioPaciente):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.btn_guardar = tk.Button(self, text="Guardar")
        self.btn_borrar = tk.Button(self, text="Borrar")
        self.btn_imc = tk.Button(self, text="IMC")
        self.btn_borrar.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_guardar.pack(side=tk.RIGHT,ipadx=5, padx=5, pady=5)
        self.btn_imc.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        
    def bindguardar(self, callback):
        self.btn_guardar.config(command=callback)
    
    def bindborrar(self, callback):
        self.btn_borrar.config(command=callback)
    
    def bindimc(self, callback):
        self.btn_imc.config(command=callback)

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Pacientes")
        self.resizable(0,0)
        self.lista = ListaPacientes(self)
        self.formulario = ActualizarPaciente(self)
        self.btn_agregar_paciente = tk.Button(self, text="Agregar Paciente")
        self.lista.pack(side=tk.LEFT, padx=10, fill=tk.Y)
        self.formulario.pack(padx=10)
        self.btn_agregar_paciente.pack(side=tk.BOTTOM, pady=5)

    def setcontrolador(self, controlador):
        self.btn_agregar_paciente.config(command=controlador.crearPaciente)
        self.lista.binddc(controlador.seleccionarPaciente)
        self.formulario.bindguardar(controlador.modificarPaciente)
        self.formulario.bindborrar(controlador.borrarPaciente)
        self.formulario.bindimc(controlador.calcularimc)
    
    def agregarPacientes(self, paciente):
        self.lista.insertar(paciente)

    def modificarPaciente(self, paciente, indice):
        self.lista.modificar(paciente, indice)
    
    def borrarPaciente(self, indice):
        self.formulario.limpiar()
        self.lista.borrar(indice)
    
    def obtenerDetalles(self):
        return self.formulario.crearpaciente()
    
    def verPaciente(self, paciente):
        self.formulario.mostrarpaciente(paciente)
