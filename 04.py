
"""

4
from collections import namedtuple
Movie = namedtuple('Movie', ['title', 'director', 'year'])
res = Movie('The Matrix', 'The Wachowskis', 1999)
print(res)

-----------------

3
from collections import Counter
temperatures = [20, 22, 20]
res = Counter(temperatures).most_common(1)
res = res[0][1], res[0][0]
print(res)

-----------------

2
from collections import Counter

monday = ['milk', 'bread']
tuesday = ['bread', 'eggs']
wednesday = ['milk', 'eggs']
thursday = ['bread', 'milk']
friday = ['eggs', 'bread']
saturday = ['bread', 'eggs']
sunday = ['bread', 'yogurt']

cnt = Counter(monday)
cnt.update(tuesday)
cnt.update(wednesday)
cnt.update(thursday)
cnt.update(friday)
cnt.update(saturday)
cnt.update(sunday)

res = [i[0] for i in cnt.most_common()[-2:][::-1]]
print(res)

-----------------

1
cities = {'СПб', 'Екб'}
countries = {frozenset(cities): None}
print(countries)

"""