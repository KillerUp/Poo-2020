import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter import messagebox

from claseFraccion import Fraccion


class Ventana(object):

    def __init__(self):
        self.__operador = '+'
        self.__ventana = tk.Tk()
        self.__ventana.title('Mi Calculadora Python')
        self.__ventana.resizable(0,0)
        fuente = font.Font(font='Arial',size=11)

        frm_panel_superior = tk.Frame(self.__ventana, bg='CornflowerBlue', relief='groove', bd=1)
        self.__buffer = tk.StringVar()
        self.__buffer.set('0.')
        self.__operacion_en_curso = tk.StringVar()
        self.__operacion_en_curso.set('0')
        lbl_operacion = tk.Label(frm_panel_superior, bg='white', textvariable=self.__operacion_en_curso, anchor='se', relief='groove', bd=4, width=32, height=1)
        lbl_operacion.config(font=('Arial', 15))
        lbl_operacion.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        frm_panel_inferior = tk.Frame(self.__ventana)
        frm_panel_numerico = tk.Frame(frm_panel_inferior, bg='CornflowerBlue', relief='groove', bd=1)
        tk.Button(frm_panel_numerico,text=7, width=5, pady=10, command= lambda: self.imprimir_operador('7'), font=fuente).grid(row=0, column=0, padx =3, pady=3)
        tk.Button(frm_panel_numerico,text=8, width=5, pady=10, command= lambda: self.imprimir_operador('8'), font=fuente).grid(row=0, column=1, padx =3, pady=3)
        tk.Button(frm_panel_numerico,text=9, width=5, pady=10, command=lambda: self.imprimir_operador('9'), font=fuente).grid(row=0, column=2, padx =3, pady=3)
        tk.Button(frm_panel_numerico,text=4, width=5, pady=10, command=lambda: self.imprimir_operador('4'), font=fuente).grid(row=1, column=0, padx =3, pady=3)
        tk.Button(frm_panel_numerico,text=5, width=5, pady=10, command=lambda: self.imprimir_operador('5'), font=fuente).grid(row=1, column=1, padx =3, pady=3)
        tk.Button(frm_panel_numerico,text=6, width=5, pady=10, command=lambda: self.imprimir_operador('6'), font=fuente).grid(row=1, column=2, padx =3, pady=3)
        tk.Button(frm_panel_numerico,text=1, width=5, pady=10, command=lambda: self.imprimir_operador('1'), font=fuente).grid(row=2, column=0, padx =3, pady=3)
        tk.Button(frm_panel_numerico,text=2, width=5, pady=10, command=lambda: self.imprimir_operador('2'), font=fuente).grid(row=2, column=1, padx =3, pady=3)
        tk.Button(frm_panel_numerico,text=3, width=5, pady=10, command=lambda: self.imprimir_operador('3'), font=fuente).grid(row=2, column=2, padx =3, pady=3)
        tk.Button(frm_panel_numerico,text='a/b', width=5, pady=10, command=lambda: self.imprimir_operador('L'), font=fuente).grid(row=3, column=0, padx =3, pady=3)
        tk.Button(frm_panel_numerico,text='0', width=5, pady=10, command=lambda: self.imprimir_operador('0'), font=fuente).grid(row=3, column=1, padx =3, pady=3)
        tk.Button(frm_panel_numerico,text='·', width=5, pady=10, command=lambda: self.imprimir_operador('.'), font=fuente).grid(row=3, column=2, padx =3, pady=3)
        frm_panel_numerico.pack( side=tk.LEFT)

        frm_panel_operadores = tk.Frame(frm_panel_inferior, bg='CadetBlue', relief='groove', bd=1)
        tk.Button(frm_panel_operadores,text='Limpiar', width=8, pady=10, command=lambda: self.limpiar(), font=fuente).grid(row=0, column=0, padx =3, pady=3)
        tk.Button(frm_panel_operadores,text='Borrar', width=8, pady=10, command=lambda: self.borrar(), font=fuente).grid(row=0, column=1, padx =3, pady=3)
        tk.Button(frm_panel_operadores,text='x', width=8, pady=10, command=lambda: self.imprimir_operador('x'), font=fuente).grid(row=1, column=0, padx =3, pady=3)
        tk.Button(frm_panel_operadores,text='%', width=8, pady=10, command=lambda: self.imprimir_operador('/'), font=fuente).grid(row=1, column=1, padx =3, pady=3)
        tk.Button(frm_panel_operadores,text='+', width=8, pady=10, command=lambda: self.imprimir_operador('+'), font=fuente).grid(row=2, column=0, padx =3, pady=3)
        tk.Button(frm_panel_operadores,text='-', width=8, pady=10, command=lambda: self.imprimir_operador('-'), font=fuente).grid(row=2, column=1, padx =3, pady=3)
        tk.Button(frm_panel_operadores,text='=', width=8, pady=10, command=lambda: self.calcular(), font=fuente).grid(row=3, column=0, padx =3, pady=3)
        tk.Button(frm_panel_operadores,text='Salir', width=8, pady=10, command=self.__ventana.destroy, font=fuente).grid(row=3, column=1, padx =3, pady=3)
        frm_panel_operadores.pack(side=tk.LEFT)

        frm_panel_superior.pack(expand=True)
        frm_panel_inferior.pack()
        tk.Button(self.__ventana,text='Simplificar Fraccion',width=40, pady=10,command= lambda:self.simplifico(), font=fuente).pack()
        self.__ventana.mainloop()

    def calcular(self):
        operandos = []
        if 'L' in self.__operacion_en_curso.get():
            op = self.__operacion_en_curso.get().split(self.__operador)
            
            for i in range(2):
                if 'L' in op[i]:
                    f = op[i].split('L')
                    aux = Fraccion(f[0], f[1])
                    operandos.append(aux)
                else:
                    aux = Fraccion(op[i])
                    operandos.append(aux)
            if self.__operador == '+':
                self.__operacion_en_curso.set(str(operandos[0] + operandos[1]))
            if self.__operador == '-':
                self.__operacion_en_curso.set(str(operandos[0] - operandos[1]))
            if self.__operador == 'x':
                self.__operacion_en_curso.set(str(operandos[0] * operandos[1]))
            if self.__operador == '/':
                self.__operacion_en_curso.set(str(operandos[0] / operandos[1]))
        else:
            operacion = eval(self.__operacion_en_curso.get().replace('x', '*'))
            self.__operacion_en_curso.set(str(float(operacion).__round__(5)))
            self.__buffer.set(self.__operacion_en_curso.get())

    def limpiar(self):
        self.__operacion_en_curso.set('0.')
        self.__buffer.set('0.')

    def borrar(self):
        texto = self.__operacion_en_curso.get()
        if texto == '0.':
            return
        else:
            texto = '{}'.format(texto[0:len(texto) - 1])
            if texto == '0' or texto == '':
                self.__operacion_en_curso.set('0.')
                self.__buffer.set('0.')
            else:
                self.__operacion_en_curso.set(texto)

    def imprimir_operador(self, operador):
        if self.__buffer.get() != '':
            if operador in ['+', 'x', '/','-']:
                self.__operador = operador
                self.__operacion_en_curso.set(self.__buffer.get() + operador)
                self.__buffer.set('')
            else:
                self.__operacion_en_curso.set('')
                self.__buffer.set('')
                texto = self.__operacion_en_curso.get()
                texto += operador
                self.__operacion_en_curso.set(texto)
            
        else:
            if operador in ['+', 'x', '/','-']:
                self.__operador = operador
                if self.__operacion_en_curso.get().count('+') > 0 or self.__operacion_en_curso.get().count('-') > 0 or self.__operacion_en_curso.get().count('x') > 0 or self.__operacion_en_curso.get().count('/') > 0:
                    messagebox.showerror(title='Error',message='Solo se puede realizar una operacion')
                    return

            texto = self.__operacion_en_curso.get()
            texto += operador
            self.__operacion_en_curso.set(texto)
    
    def simplifico(self):
        if 'L' in self.__operacion_en_curso.get():
            op = self.__operacion_en_curso.get().split('L')
            f = Fraccion(op[0],op[1])
            f.simplificar()
            self.__operacion_en_curso.set(str(f))

        if '/' in self.__operacion_en_curso.get():
            op = self.__operacion_en_curso.get().split('/')
            f = Fraccion(op[0],op[1])
            f.simplificar()
            self.__operacion_en_curso.set(str(f))
        




            
            
