﻿def hello():
    print("Ricardo Quinzo")

def peter():
    print("Pedro Muñoz")
    
def daniel():
    print("Daniel Acevedo")

def estefa():
    print("Estefania Aguilar")

def genaro():
    print("Daniel Flores")

from tkinter import *

tk=Tk()

btn = Button(tk, text="Ricardo", command=hello)
btn2 = Button(tk, text= "Pedro Muñoz", command = peter)
btn3 = Button(tk, text= "Daniel", command = daniel)
btn4 = Button(tk, text= "Estefania", command = estefa)
btn5 = Button(tk, text= "Daniel Flores", command = genaro)

btn.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()




