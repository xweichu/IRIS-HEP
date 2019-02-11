from MyBasket import MyBasket

mb = MyBasket()
print(mb.toString())

file = open('test.txt','r')
mb.restore(file)
print(mb.toString())
mb.restore(file)
print(mb.toString())
mb2 = MyBasket()
print(mb > mb2)

