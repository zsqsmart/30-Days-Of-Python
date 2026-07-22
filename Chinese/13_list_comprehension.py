# 列表推导式

from collections.abc import Callable
from typing import cast

language = 'python'
words = list(language)
print(type(words))
print(words)

words = [i for i in language]
print(type(words))
print(words)

numbers = [i for i in range(11)]
print(numbers)

squares = [pow(i, 2) for i in range(11)]
print(squares)

numbers = [(i, i**2) for i in range(11)]
print(numbers)

even_numbers = [i for i in range(11) if i % 2 == 0]
print(even_numbers)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)


def add_two_numbers(a: int, b: int):
    total = a + b
    return total


print((lambda a, b: a + b)(2, 3))


def power(x: int) -> Callable[[int], int | float]:
    return lambda n: cast(int | float, x**n)


cube = power(2)(3)  # 函数 power 现在需要两个单独的括号中的参数
print(cube)

# 使用列表推导式过滤出列表中的负数和零：
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_numbers = [number for number in numbers if number > 0]

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [number for rows in list_of_lists for row in rows for number in row]

print(flattened_list)

# 使用列表推导式创建以下元组列表：

# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

numbers = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
numbers = [(i, *(i**exponent for exponent in range(6))) for i in range(11)]

print(numbers)


countries = [[('芬兰', '赫尔辛基')], [('瑞典', '斯德哥尔摩')], [('挪威', '奥斯陆')]]

flattened_list = [list(country) for row in countries for country in row]
print(flattened_list)

countries = [[('芬兰', '赫尔辛基')], [('瑞典', '斯德哥尔摩')], [('挪威', '奥斯陆')]]
dict_list: list[dict[str, str]] = [
    {'国家': country[0], '首都': country[1]} for row in countries for country in row
]
print(dict_list)

names = [
    [('Asabeneh', 'Yetayeh')],
    [('David', 'Smith')],
    [('Donald', 'Trump')],
    [('Bill', 'Gates')],
]
flattened_list = [' '.join(list(name)) for row in names for name in row]
print(flattened_list)
