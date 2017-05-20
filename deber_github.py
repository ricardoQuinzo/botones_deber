def hello():
    print("Ricardo Quinzo")

def peter():
    print("Pedro Muñoz")

from tkinter import *

tk=Tk()

btn = Button(tk, text="Ricardo", command=hello)
btn2 = Button(tk, text= "Pedro Muñoz", command = peter)

btn.pack()
btn2.pack()




