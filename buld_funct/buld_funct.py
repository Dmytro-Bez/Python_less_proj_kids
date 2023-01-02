#baf = dir(['Це якщо не ти дуже це хороший читаєш спосіб то заховати щось повідомлення негаразд'])
#print(baf)

#print(help(baf))

##################
text=open('test.txt')
test_text=text.read()
text.close()
text=open('test1.txt', 'w')
text.write(test_text)
text.close()
