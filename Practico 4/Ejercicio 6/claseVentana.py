import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox, ttk

from claseProvincia import Provincia

class ListaProvincias(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master=master)
        self.lista = tk.Listbox(self, **kw)
        scroll = tk.Scrollbar(self, command=self.lista.yview)
        self.lista.config(yscrollcommand=scroll.set)
        self.lista.pack(side=tk.LEFT, fill=tk.Y, pady=5)
        scroll.pack(side=tk.LEFT, fill=tk.Y, pady=5)
    
    def insertar(self, provincia, indice=tk.END):
        self.lista.insert(indice, provincia)
    
    def borrar(self, indice):
        self.lista.delete(indice, indice)

    def modificar(self, provincia, indice):
        self.borrar(indice)
        self.insertar(provincia, indice)
    
    def binddc(self, callback):
        manejador = lambda _: callback(self.lista.curselection()[0])
        self.lista.bind("<Double-Button-1>", manejador)

class FormularioProvincias(tk.LabelFrame):
    
    def __init__(self, master=None, campos=(), **kw):
        super().__init__(master=master, text="Provincia", padx=10, pady=10,  **kw)
        self.campos = ('Nombre', 'Capital', 'Cantidad de habitantes', 'Cantidad de departamentos/partidos') + campos
        self.frame = tk.Frame(self)
        self.entradas = list(map(self.crearcampo, enumerate(self.campos)))
        self.frame.pack()

    def crearcampo(self, campo):
        posicion, texto = campo
        lbl_texto = tk.Label(self.frame, text=texto)
        ent_entrada = tk.Entry(self.frame, width=30,bg='White')
        lbl_texto.grid(row=posicion, column=0, pady=5)
        ent_entrada.grid(row=posicion, column=1, pady=5)
        return ent_entrada
    
    def mostrarprovincia(self, provincia,valores_clima=()):
        valores = (provincia.getnombreprovincia(), provincia.getnombrecapital(), provincia.gethabitantes(), provincia.getdepartamentos()) + valores_clima
        for entrada, valor in zip(self.entradas, valores):
            entrada.delete(0, tk.END)
            entrada.insert(0, valor)
    
    def crearprovincia(self):
        valores = [entrada.get() for entrada in self.entradas]
        provincia = None
        try:
            provincia = Provincia(*valores)
        except ValueError as e:
            messagebox.showerror("Valores no validos", str(e), parent=self)
        
        return provincia

    def limpiar(self):
        for entrada in self.entradas:
            entrada.delete(0, tk.END)

class FormularioClima(FormularioProvincias):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, campos=('Temperatura','Sensación Termica','Humedad'),**kw) 

    def mostrarprovincia(self,provincia,valores_clima):
        super().mostrarprovincia(provincia, valores_clima)
    

class nuevaprovincia(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.resizable(0,0)
        self.provincia = None
        self.formulario = FormularioProvincias(self)
        self.btn_confirmar = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.formulario.pack()
        self.btn_confirmar.pack()

    def confirmar(self):
        self.provincia = self.formulario.crearprovincia()
        if self.provincia:
            self.destroy()
    
    def mostrar(self):
        self.grab_set()
        self.wait_window()
        return self.provincia


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Pacientes")
        self.resizable(0,0)
        self.lista = ListaProvincias(self)
        self.formulario = FormularioClima(self)
        self.btn_agregar_provincia = tk.Button(self, text="Agregar Provincia")
        self.lista.pack(side=tk.LEFT, padx=10, fill=tk.Y)
        self.formulario.pack(padx=10)
        self.btn_agregar_provincia.pack(side=tk.BOTTOM, pady=5)

    def setcontrolador(self, controlador):
        self.btn_agregar_provincia.config(command=controlador.crearProvincia)
        self.lista.binddc(controlador.seleccionarProvincia)

    
    def agregarprovincias(self, provincia):
        self.lista.insertar(provincia)


    def obtenerDetalles(self):
        return self.formulario.crearprovincia()

    
    def verprovincia(self, paciente,valores_clima):
        self.formulario.mostrarprovincia(paciente,valores_clima)
