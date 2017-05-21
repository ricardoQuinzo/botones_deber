def hello():
    print("Ricardo Quinzo")

def peter():
    print("Pedro Muñoz")
    
def daniel():
    print("Daniel Acevedo")

from tkinter import *

tk=Tk()

btn = Button(tk, text="Ricardo", command=hello)
btn2 = Button(tk, text= "Pedro Muñoz", command = peter)
btn3 = Button(tk, text= "Daniel", command = daniel)

btn.pack()
btn2.pack()
btn3.pack()



