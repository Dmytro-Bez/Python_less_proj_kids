#Box

import turtle

t=turtle.Pen()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

#Test book
t.clear()
t.reset()
#povorot pom line back
t.backward(100)
#pidnyt do verh line
t.up()
t.right(90)
#line pered
t.forward(20)
t.left(90)
#Vozvrat line
t.down()
t.forward(100)

#Cvadrat
t.clear()
t.reset()
t.forward(50)
t.left(90)
t.forward(20)
t.left(-90)
t.backward(50)
t.left(-90)
t.forward(20)

#Trikytnik 
t.reset()
t.forward(62)
t.left(90)
t.forward(62)
t.left(-45)
t.forward(-86)

#Prist
t.reset()
t.forward(62)
t.left(-90)
t.up()
t.forward(12)
t.left(90)
t.forward(12)
t.left(-90)
t.down()
t.forward(62)
t.left(-90)
t.up()
t.forward(12)
t.left(90)
t.forward(12)
t.left(90)
t.down()
t.backward(62)
t.up()
t.backward(12)
t.left(90)
t.forward(12)
t.down()
t.forward(62)

a=1
print(a)