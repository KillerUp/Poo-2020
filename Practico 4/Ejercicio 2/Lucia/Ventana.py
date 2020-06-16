import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import Tk,StringVar
from tkinter.constants import *
import requests

class Ventana(object):
    
    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title('Conversor de Moneda')
        self.ventana_principal.geometry('300x150')
        self.ventana_principal.resizable(0,0)
        self.__dolar = StringVar()
        self.__Peso = StringVar()
        self.__dolar.trace('w', self.calcular)
        self.__DolaresEntry = tk.Entry(self.ventana_principal,width=15,textvariable=self.__dolar)
        self.__DolaresEntry.place(x='100',y='30')
        lbl_a = tk.Label(self.ventana_principal,text='dolares')
        lbl_a.place(x='160',y='30')
        lbl_b = tk.Label(self.ventana_principal,text='Es equivalente a:')
        lbl_b.place(x='7',y='57')
        lbl_c = tk.Label(self.ventana_principal, textvariable= self.__Peso)
        lbl_c.place(x='100',y='57')
        lbl_d = tk.Label(self.ventana_principal,text='Pesos')
        lbl_d.place(x='170',y='57')
        salir = tk.Button(self.ventana_principal,text='   Salir   ',command=self.ventana_principal.destroy)
        salir.place(x='170',y='80')
        self.ventana_principal.mainloop()

    def calcular(self,*args):
        if self.__DolaresEntry.get()!='':
            try:
                valor = float(self.__DolaresEntry.get())
                r = requests.get('https://www.dolarsi.com/api/api.php?type=dolar')
                dic = r.json()
                i = 0
                while (i < len(dic)) & (dic[i]['casa']['nombre'] != 'Oficial'):
                    i +=1
                if i < len(dic):
                    p = float(dic[i]['casa']['venta'].replace(',' , '.'))
                    self.__Peso.set(round(p*valor,2))
            except ValueError:
                messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numérico')
                self.__dolar.set('')
                self.__DolaresEntry.focus()
        else:
            self.__Peso.set('')

