#Class test
# class Тварина(set):
#     print("Я тварина")
#     def око(self):
#         print("Я бачу!")
#
# тваринака = Тварина()
# тваринака.око()

class Предмет:
    pass

class Неживий(Предмет):
    pass

class Живі(Предмет):
    pass

class Тротуари(Неживий):
    pass

class Тварина(Живі):
    def дихає(self):
        pass

    def ходити(self):
        pass

    def рухається(self):
        pass

    def харчується_їжею(self):
        pass

class Савці(Тварина):
    def годує_дитину_молоком(self):
        pass

class Жирафи(Савці):
    плями = 0
    def __init__(self, плями):
        self.жирафені_плями=плями

    def дихає(self):
        pass

    def їсть_лисття_з_дерева(self):
        self.харчується_їжею()

    def шукає_їжу(self):
        self.рухається()
        print("Я знайшов їжу!")
        self.харчується_їжею()

    def танцювати(self):
        self.рухається()
        self.рухається()
        self.рухається()
        self.рухається()

#жаджи = Жирафи(100)
#print(жаджи.жирафені_плями)


import turtle
one = turtle.Pen()
one.forward(100)
one.left(90)
one.forward(20)
one.backward(40)
one.left(90)
one.backward(40)
one.left(180)

two = turtle.Pen()
two.forward(100)
two.left(-90)
two.backward(20)
two.left(-90)
two.backward(40)
two.left(-180)

thee = turtle.Pen()
thee.forward(80)
thee.left(90)
thee.backward(40)
thee.left(-90)
thee.forward(80)

four = turtle.Pen()
four.forward(80)
four.left(-90)
four.backward(40)
four.left(-90)
four.backward(80)
four.left(-180)
