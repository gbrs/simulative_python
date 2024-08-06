# начать с задачи 12

def count_banknotes(amount, num_100_available, num_50_available, num_10_available):
    amount_100 = min(num_100_available, amount // 100)
    amount_50 = min(num_50_available, (amount - 100 * amount_100) // 50)
    amount_10 = (amount - 100 * amount_100 - 50 * amount_50) // 10
    return amount_100, amount_50, amount_10


print(count_banknotes(450, 8, 50, 70))

"""
https://lms.simulative.ru/demo/10/9000/7WLHIGNL3F
------------------



------------------



------------------



------------------



------------------

12
def count_banknotes(amount, num_100_available, num_50_available, num_10_available):
    amount_100 = min(num_100_available, amount // 100)
    amount_50 = min(num_50_available, (amount - 100 * amount_100) // 50)
    amount_10 = (amount - 100 * amount_100 - 50 * amount_50) // 10
    return amount_100, amount_50, amount_10


print(count_banknotes(450, 8, 50, 70))

------------------

5
def average(*args):
    return sum(args) / len(args)


print(average(23, 1, 1, 23))

------------------

4
def digit_sum(n):
    from functools import reduce
    return reduce(lambda cnt, x: cnt + x, list(map(int, str(n))), 0)


number = 9821
print(digit_sum(number))

------------------

3
def always500(*args):
    return 500

print(always500())
print(always500("string", 102, True))
print(always500([2, 7], {3: 2}))
print(always500("Hello, world!"))

"""