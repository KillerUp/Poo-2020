import datetime as dt
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

import requests


class Ventana(object):
    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.__dolar = None
        self.__compra = None
        self.__venta = None
        self.ventana_principal.title('Valores dolar')
        self.ventana_principal.configure(bg = 'MistyRose')
        self.ventana_principal.resizable(0,0)

        self.ultima_actualizacion = tk.StringVar()
        self.ultima_actualizacion.set('0-0-0')

        fuente = tkFont.Font(family="Copperplate Gothic Bold", size=20)
        fuente2 = tkFont.Font(family="Gabriola", size=25)
        self.fuente3 = tkFont.Font(family="Copperplate Gothic Bold", size=15)
        lbl_a = tk.Label(self.ventana_principal,text='Cotizaciones de dolar',bg='#f5f5f5',font=fuente)
        opts = { 'ipadx': 10, 'ipady': 10, 'fill': tk.BOTH }
        lbl_a.pack(side=tk.TOP, **opts)

        self.frm_valores = tk.Frame(self.ventana_principal, bg = 'MistyRose')
        lbl_b = tk.Label(self.frm_valores,text='Dolar',bg= 'MistyRose',foreground='Gray', font=fuente2)
        lbl_b.grid(row=0, column=0, ipadx=40, sticky="W")
        lbl_c = tk.Label(self.frm_valores,text='Compra',bg='MistyRose',foreground='Gray',font=fuente2)
        lbl_c.grid(row=0, ipadx=40, column=1, sticky='W')
        lbl_d = tk.Label(self.frm_valores,text='Venta',bg='MistyRose',foreground='Gray',font=fuente2)
        lbl_d.grid(row=0, column=2, ipadx=40, sticky='W')
        self.frm_valores.pack(expand=True)

        self.frm_actualizacion = tk.Frame(self.ventana_principal)
        btn_actualizar = tk.Button(self.frm_actualizacion,text='Actualizar', bg='Gray',command = lambda: self.valor())
        btn_actualizar.pack(side=tk.LEFT)

        frm_ultima_actualizacion = tk.Frame(self.frm_actualizacion)
        tk.Label(frm_ultima_actualizacion, text='Ultima actualizacion:').pack()
        lbl_ultima_actualizacion = tk.Label(frm_ultima_actualizacion, textvar=self.ultima_actualizacion)
        lbl_ultima_actualizacion.pack()
        frm_ultima_actualizacion.pack(side=tk.RIGHT)
        self.frm_actualizacion.pack(fill=tk.X)

        self.valor()
        self.ventana_principal.mainloop()

    def valor(self):
        r = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
        dic = r.json()
        i= 0
        dolar = ''
        compra=''
        venta=''
        while i < len(dic):
            if dic[i]["casa"]["nombre"].find('Dolar') != -1 and dic[i]["casa"]["compra"] != 0 and dic[i]["casa"]["venta"] != 0:
                dolar = dic[i]["casa"]["nombre"]
                compra = dic[i]["casa"]["compra"]
                venta = dic[i]["casa"]["venta"]

                tk.Label(self.frm_valores, text=str(dolar), font=self.fuente3, bg = 'MistyRose').grid(row=i+1, column=0, ipadx=40, ipady=25, sticky="W")
                tk.Label(self.frm_valores, text=str(compra), font=self.fuente3, bg = 'MistyRose').grid(row=i+1, column=1, ipadx=40, ipady=25, sticky='W')
                tk.Label(self.frm_valores, text=str(venta), font=self.fuente3, bg = 'MistyRose').grid(row=i+1, column=2, ipadx=40, ipady=25, sticky='W')
                ttk.Separator(self.frm_valores, orient=tk.HORIZONTAL).grid(row=i+2, columnspan=3)

                i+=1
            else:
                i+=1

        a = dt.datetime.today()

        hoy = '{}/{}/{}, {}:{}:{}'.format(a.day, a.month, a.year, a.hour, a.minute, a.second)

        self.ultima_actualizacion.set(hoy)
