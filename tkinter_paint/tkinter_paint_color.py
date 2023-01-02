from tkinter import *
import random
tk=Tk()
###
canvas=Canvas(tk,width=500,heigh=500)
canvas.pack()

def random_rectangle(width,heigh,fill_color):
    x1=random.randrange(width)
    y1=random.randrange(heigh)
    x2=random.randrange(x1+random.randrange(width))
    y2=random.randrange(y1+random.randrange(heigh))
    canvas.create_rectangle(x1,y1,x2,y2,fill=fill_color)
