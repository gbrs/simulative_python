# Было: Просто еще одна обычная строка
# Стало: Просто-еще-одна-обычная-строка

s = 'это повтор повтор и еще повтор'
start = s.find('повтор', 5)
print(start)

"""

https://lms.simulative.ru/demo/10/9000/7WLHIGNL3F
-----------------------



-----------------------



-----------------------



-----------------------



-----------------------



-----------------------

27
s = 'это повтор повтор и еще повтор'
start = s.find('повтор', 5)

-----------------------

25
s = 'Просто еще одна обычная строка'
s_splitted = s.split()
s = '-'.join(s_splitted)

-----------------------

22
s = '      это строка    с большими пробелами      '
s = s.strip()

-----------------------

21
num = 5
s1 = 'Это'
s = '{S1} число {N}'.format(S1=s1, N=num)

-----------------------

19
s = '''это первая строка
это вторая строка
это третья строка'''

-----------------------

18
s = "сначала сделаем \tтабуляцию\nа теперь перейдем на новую строку"

-----------------------

14
s = str(1e-5)

-----------------------

8
c = 5 + 3j
c1 = c.conjugate()

-----------------------

7
c = 5 + 3j
r = c.real
i = c.imag

-----------------------

6
c = 5 + 3j
c1 = 1j
c2 = 6 + 0j

-----------------------

5
from math import floor, e
t = floor(e)

-----------------------

4
t = 3.14159_26535
t_rounded = round(t, 3)

-----------------------

3
t = 0.00002

-----------------------

2
y = 3
t = type(y)

-----------------------

1
x = 10

"""
