



"""

https://lms.simulative.ru/demo/10/9000/7WLHIGNL3F

------------------

20
min_grades = {'Русский язык': 40, 'Математика': 39, 'Физика': 42}

res = min(min_grades, key=lambda x: min_grades[x])
min_grades_2024 = {i: None for i in min_grades}

print(min_grades_2024)

------------------

19
january_spendings = {"CategoryA": 100, "CategoryB": 200}
february_spendings = {"CategoryB": 150, "CategoryC": 250}
march_spendings = {"CategoryF": 400, "CategoryA": 120}

common_spendings = {}
common_spendings.update(january_spendings)
common_spendings.update(february_spendings)
common_spendings.update(march_spendings)


print(common_spendings)

------------------

15
lunch_menu = {"hamburger", "fries", "salad", "soup", "soft drink"}
dinner_menu = {"steak", "chicken", "pasta", "salad", "vegetables", "wine"}
customer_order = {"hamburger", "fries", "salad"}

print(f"Ваш заказ может быть подан на обед: {customer_order <= lunch_menu}")
print(f"Ваш заказ может быть подан на ужин: {customer_order <= dinner_menu}")

------------------

11
a = {1, 2}
b = {1, 5}
c = {4, 5}

print('2 данных множества имеют общие элементы:')
print(f'A и B: {bool(a & b)}')
print(f'A и C: {bool(a & c)}')
print(f'B и C: {bool(b & c)}')

------------------

10
olympics = ('UK', 'Germany', 'Austria', 'UK', 'Sweden', 'Germany')

res = []
for country in ('Russia', 'Austria', 'USA', 'Germany'):
    res.append([country, olympics.count(country)])

res = tuple(res)

print(res)

------------------

9
N = 15
store = (['кока-кола', 42], ['вода', 60], ['кофе', 15], ['чай', 5], ['сок', 23])
new_store = tuple([i[0], i[1] - N] for i in store if i[1] > 15)
needed = tuple(i[0] for i in store if i[1] <= 15)

print(new_store)
print(needed)

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



