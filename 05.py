def digit_sum(n):
    from functools import reduce
    return reduce(lambda cnt, x: cnt + x, list(map(int, str(n))), 0)


number = 9821
print(digit_sum(number))

"""
https://lms.simulative.ru/demo/10/9000/7WLHIGNL3F
------------------



------------------



------------------



------------------



------------------



------------------



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