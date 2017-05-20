def hello():
    print("Ricardo Quinzo")

from tkinter import *

tk=Tk()
btn = Button(tk, text="Ricardo", command=hello)
btn.pack()
