# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 20:35:34 2019

@author: cristiano_001325
"""

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Bem Vindo")
window.geometry('350x200')
lbl = Label(window, text="Digite um Número")
lbl.grid(column=0, row=0)
numero = Entry(window,width=10)
numero.grid(column=1, row=0)
def clicked():
 
    messagebox.showinfo('Numero ao Quadrado é: ', 'resulado é: '+ numero.get())
 
btn = Button(window, text="OK", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()