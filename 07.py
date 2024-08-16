"""

"""

"""
------------------



------------------



------------------



------------------

12
def args_processing(*args, **kwargs):
    result = 'Позиционные аргументы:\n'
    for i in args:
        result += str(i) + '\n'
    result += 'Именованные аргументы:\n'
    for k, v in kwargs.items():
        result += f"ключ - {k}, значение - {v}\n"
    return result.strip()


print(args_processing(1, [1], a=[2, 3], b='s'))

"""