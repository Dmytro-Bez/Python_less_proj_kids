#from tkinter import *
#tk=Tk()
#butt=Button(tk, text='Pleas touch me')
#butt.pack()

def здоров():
    print("Здоров")

from tkinter import *
import random
tk=Tk()
butt=Button(tk, text="Pleas touch me", command=здоров)
butt.pack()
###
canvas=Canvas(tk,width=500,heigh=500)
canvas.pack()
canvas.create_line(0,0,500,500)
#canvas.create_rectangle(80,10,100,50)

