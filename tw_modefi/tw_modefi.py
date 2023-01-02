import turtle
t=turtle.Pen()

#t.forward(50)
#t.left(45)
#t.forward(50)
#t.left(45)
#t.forward(50)
#t.left(45)
#t.forward(50)
#t.left(45)
#t.forward(50)
#t.left(45)
#t.forward(50)
#t.left(45)
#t.forward(50)
#t.left(45)
#t.forward(50)
#t.left(45)

def n_8(a,b):
    for x in range(a,b):
        t.forward(50)
        t.left(45)  

##########################
def n_8_color(sep,sip):
    if sip==True:
        t.begin_fill()
    for x in range(1,9):  
        t.forward(sep)
        t.left(45)
    if sip==True:
            t.end_fill()
t.reset()

def start_p(sep,sip):
    for x in range(sep,sip):
        t.forward(50)
        t.left(225)

#############################

