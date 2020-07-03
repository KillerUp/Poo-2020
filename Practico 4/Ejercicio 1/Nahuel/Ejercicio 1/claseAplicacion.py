import tkinter as tk
from tkinter import messagebox

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("660x350")
        self.resizable(0,0)
        self.__resultado = tk.StringVar()
        self.__resultado.set('')
        self.__altura = tk.StringVar()
        self.__altura.set('')
        self.__peso = tk.StringVar()
        self.__peso.set('')
        self.__texto = tk.StringVar()
        self.__texto.set('')
        self.__frm_resultado = tk.Frame()
        tk.Label(self, text="Calculadora de IMC", font=("Cambria", 32)).pack()

        frm_inout = tk.Frame(self)
        tk.Label(frm_inout, text="Altura:", font=('Consolas', 26)).grid(row=0, column=0, sticky="W", pady=5)
        self.__ent_altura = tk.Entry(frm_inout, font=('Consolas', 26), relief='sunken', textvar=self.__altura)
        self.__ent_altura.grid(row=0, column=1, sticky="E", pady=5)
        tk.Label(frm_inout, text="cm", font=('Consolas', 26), relief='sunken').grid(row=0, column=2, pady=5, sticky='W')
        tk.Label(frm_inout, text="Peso:", font=('Consolas', 26)).grid(row=1, column=0, sticky="W", pady=5)
        self.__ent_peso = tk.Entry(frm_inout, font=('Consolas', 26), relief='sunken', textvar=self.__peso)
        self.__ent_peso.grid(row=1, column=1, sticky="E", pady=5)
        tk.Label(frm_inout, text="Kg", font=('Consolas', 26), relief='sunken').grid(row=1, column=2, sticky='W', pady=5)
        frm_inout.pack()

        frm_botones = tk.Frame(self)
        tk.Button(frm_botones, text="Calcular", font=('Consolas', 18), command=self.calcular, width=20).grid(row=0, column=0, sticky="E", pady=5, padx=10)
        tk.Button(frm_botones, text="Limpiar", font=('Consolas', 18), command=self.limpiar, width=20).grid(row=0, column=1, sticky="W", pady=5, padx=10)
        frm_botones.pack()

    def limpiar(self):
        self.__ent_altura.delete(0, tk.END)
        self.__ent_peso.delete(0, tk.END)
        self.__resultado.set('')
        self.__texto.set('')
        self.__frm_resultado.destroy()

    def calcular(self):
        try:
            altura = int(self.__altura.get())/100
            peso = float(self.__peso.get())
        except:
            messagebox.showerror(title="Error de entrada", message="La altura debe ser en centímetros.\nEl peso debe ser en kilogramos.")
        else:
            resultado = peso / (altura * altura)
            self.__texto.set('Tu indice de Masa Corporal (IMC) es:')
            self.__resultado.set('{} Kg/m2'.format(round(resultado, 2)))
            self.__frm_resultado.destroy()

            self.__frm_resultado = tk.Frame(self, bg='LightGreen')
            lbl_texto = tk.Label(self.__frm_resultado, textvar=self.__texto, font=('Arial', 18), bg='LightGreen')
            lbl_texto.pack()
            lbl_resultado = tk.Label(self.__frm_resultado,textvar=self.__resultado, font=('Arial Black', 16), bg='LightGreen')
            lbl_resultado.pack()
            composicion = tk.StringVar()
            composicion.set(self.composicion(resultado))
            lbl_composicion= tk.Label(self.__frm_resultado,textvar=composicion, font=('Arial', 26), bg='LightGreen')
            lbl_composicion.pack()
            self.__frm_resultado.pack(pady=5)
            
    def composicion(self, imc):
        cadena = 'Peso '
        if imc < 18.5:
            cadena += 'inferior al normal.'
        elif imc >= 18.5 and imc <= 24.9:
            cadena += 'normal.'
        elif imc >= 25 and imc <= 29.9:
            cadena += 'superior al normal.'
        else:
            cadena = 'Obesidad.'
        
        return cadena