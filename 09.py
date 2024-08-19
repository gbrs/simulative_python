"""
Напишите функцию is_file_empty, которая принимает путь к файлу file_path и проверяет, является ли он пустым.
Функция должна возвращать True если файл пуст, и False если в нем есть какие-либо данные.
"""




"""
------------------



------------------



------------------

2
def is_file_empty(file_path):
    import os
    if os.path.getsize(file_path):
        return False
    else:
        return True


file_path = './a_few_lines_of_text.txt'

print(is_file_empty(file_path))

------------------

1
lst = []

with open('a_few_lines_of_text.txt', encoding='utf-8') as f:
    for i, line in enumerate(f):
        lst.append(f"{i + 1}: " + line)

with open('numbered_lines_of_text.txt', 'wt', encoding='utf-8') as f:
    for i in lst:
        f.write(i)

"""