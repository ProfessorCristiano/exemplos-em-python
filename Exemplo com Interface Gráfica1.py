# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 20:35:34 2019

@author: cristiano_001325
"""

from tkinter import *

window = Tk()
window.title("Bem Vindo")
window.geometry('350x200')

lb1 = Label(window, text="Digite um Número")
lb1.grid(column=0, row=0)
lb2 = Label(window, text="O Quadrado do Numero é")
lb2.grid(column=0, row=1)
lb3 = Label(window, text="")
lb3.grid(column=1, row=2)

numero = Entry(window,width=10)
numero.grid(column=1, row=0)

def clicked():
    n=int(numero.get())
    quadrado=n*n
    lb3.configure(text= quadrado)
 
btn = Button(window, text="OK", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()