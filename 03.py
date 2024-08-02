'''
Сделал 4
'''

cart = []
a = 'a'
b = ['b1', 'b2']
c = 'c'

cart.append(a)
cart1 = cart[:]

cart1.extend(b)

cart2 = cart1[:]
cart2.insert(1, c)

print(cart, cart1, cart2)

"""



------------------



------------------



------------------



------------------



------------------



------------------



------------------

4
cart = []
a = 'a'
b = ['b1', 'b2']
c = 'c'

cart.append(a)
cart1 = cart[:]

cart1.extend(b)

cart2 = cart1[:]
cart2.insert(1, c)

print(cart, cart1, cart2)

------------------

2
current = ['Молоко', 'Хлеб', 'Яйца', 'Сахар', 'Соль']
postavka = ['Мука', 'Рис', 'Спагетти', 'Картофель', 'Лук']
a = 'Кофе'

current.extend(postavka)
postavka.clear()
postavka.append(a)

print(current)
print(postavka)

------------------
"""



