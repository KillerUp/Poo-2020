import tkinter as tk
from Nutricion import Nutricionista
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk, messagebox


class Ventana(object):
    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.imc = Nutricionista()
        self.cadena = ''
        self.valor = 0
        self.lbl_f = None
        self.ventana_principal.title('Calculadora')
        self.ventana_principal.configure(bg = 'White')
        self.ventana_principal.geometry('750x350')
        self.ventana_principal.resizable(0,0)
        fuente = tkFont.Font(family="Arial", size=20)
        fuente2 = tkFont.Font(family="Calibri", size=15)
        lbl_a = tk.Label(self.ventana_principal,text='Calculadora de IMC',bg='#f5f5f5',font=fuente)
        opts = { 'ipadx': 10, 'ipady': 10, 'fill': tk.BOTH }
        lbl_a.pack(side=tk.TOP, **opts)
        lbl_b = tk.Label(self.ventana_principal,text='Altura:',bg= 'White',foreground='Gray', font=fuente2)
        lbl_b.place(x='10',y='100')
        altura = StringVar()
        self.AlturaEntry = tk.Entry(self.ventana_principal, width=103, textvariable=altura)
        self.AlturaEntry.place(x='80',y='107')
        lbl_c = tk.Label(self.ventana_principal,text='Cm',bg='#f5f5f5',foreground='Gray',font=fuente2)
        lbl_c.place(x='705',y='100')
        lbl_d = tk.Label(self.ventana_principal,text='Peso:',bg='White',foreground='Gray',font=fuente2)
        lbl_d.place(x='10',y='150')
        peso = StringVar()
        self.PesoEntry = tk.Entry(self.ventana_principal,width=103,textvariable=peso)
        self.PesoEntry.place(x='80',y='157')
        lbl_e = tk.Label(self.ventana_principal,text=' Kg ',bg='#f5f5f5',foreground='Gray',font=fuente2)
        lbl_e.place(x='704',y='150')
        boton_calcular = tk.Button(self.ventana_principal,text='             Calcular           ', bg='#5cb85c',foreground='White',command = lambda: self.calculaimc())
        boton_calcular.place(x='170',y='200') 
        boton_limpiar = tk.Button(self.ventana_principal,text='             Limpiar           ',bg='#5cb85c',foreground='White',command = lambda: self.limpiar())
        boton_limpiar.place(x='480',y='200')
        self.ventana_principal.mainloop()

    def calculaimc(self):
        try:
            float(self.PesoEntry.get())
            float(self.AlturaEntry.get())
        except:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')
        else:
            self.valor, self.cadena = self.imc.calcula(self.PesoEntry.get(),self.AlturaEntry.get())
            fuente = tkFont.Font(family="Eras Light ITC", size=20)
            self.lbl_f  = tk.Label(self.ventana_principal,text='Tu indice de masa corporal (IMC) es {} Kg/m2 \n {}'.format(round(self.valor,2),self.cadena),bg='AliceBlue',foreground='Green',font=fuente)
            self.lbl_f.place(x='113',y='250')
    
    def limpiar(self):
        self.AlturaEntry.delete(0, tk.END)
        self.PesoEntry.delete(0, tk.END)
        self.lbl_f.place_forget()
        

