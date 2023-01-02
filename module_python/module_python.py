class Animal:
    def __init__(self,вид,кількість_ніг,забарвлення):
        self.вид = вид
        self.кількість_ніг=кількість_ніг
        self.забарвлення=забарвлення

import copy
rappi=Animal('Gip',6,'red')
rappi=copy.copy(rappi)
print(rappi.вид)
print(rappi.кількість_ніг)
print(rappi.забарвлення)

import random
number=random.randint(1,9)
while True:
    print('Вгадай число між 1 і 9')
    здогад=input()
    i=int(здогад)
    if i==number:
        print('Правильно здогад')
        break
    elif i<number:
        print('Бери вижки')
    elif i > number:
        print('Бери нижче')

        
