"""

"""


"""
------------------



------------------



------------------



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