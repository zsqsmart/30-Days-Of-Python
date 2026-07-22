import math
import random
import string
from math import ceil, floor, sqrt
from math import pi as PI

print(PI)
print(sqrt(2))
print(pow(2, 3))
print(floor(9.81))
print(ceil(9.81))
print(math.log10(100))


print(string.ascii_letters)
print(string.digits)
print(string.punctuation)


def random_user_id(length: int = 6):
    words = string.ascii_letters + string.digits
    user_id = ''
    for _ in range(length):
        user_id += random.choice(words)
    return user_id


print(random_user_id())


def user_id_gen_by_user():
    while True:
        try:
            id_len = int(input('Enter the length of id: '))
            id_count = int(input('Enter the number of id: '))
            if id_len <= 0 or id_count <= 0:
                print('Length and count must be greater than 0')
                continue
            ids: list[str] = []
            for _ in range(id_count):
                ids.append(random_user_id(id_len))
            return '\n'.join(ids)

        except ValueError:
            print('Invalid input. Please enter a valid number.')
            continue


# print(user_id_gen_by_user())


def list_of_hexa_colors(length: int = 10):
    letters = string.hexdigits[:16]
    colors: list[str] = []
    for _ in range(length):
        color = '#'
        for _ in range(6):
            color += random.choice(letters)
            colors.append(color)
    return colors


print(list_of_hexa_colors())


# 返回一个数组中的任意数量的 RGB 颜色
def list_of_rgb_colors(length: int = 10):
    colors: list[tuple[int, int, int]] = []
    for _ in range(length):
        color: tuple[int, int, int] = (
            random.randint(0, 255),
            random.randint(0, b=255),
            random.randint(0, 255),
        )
        colors.append(color)
    return colors


print(list_of_rgb_colors())


# 可以生成任意数量的十六进制或 RGB 颜色
def generate_colors(color_type: str, length: int = 10):
    if color_type == 'hexa':
        return list_of_hexa_colors(length)
    elif color_type == 'rgb':
        return list_of_rgb_colors(length)
    else:
        return 'Invalid color type. Please enter "hexa" or "rgb".'


print(generate_colors('hexa', length=3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))


# 练习：级别 3


# 调用你的函数 shuffle_list，它接受一个列表作为参数并返回一个打乱的列表。
def shuffle_list[T](items: list[T]) -> list[T]:
    result = items.copy()
    random.shuffle(result)
    return result


print(shuffle_list([1, 2, 3, 4, 5]))


# 在 0-9 的范围内返回七个随机数的数组。所有数字必须是唯一的
def unique_random_numbers(length: int = 7):
    if not 0 <= length <= 10:
        raise ValueError('length must be between 0 and 10')

    return random.sample(range(10), length)


print(unique_random_numbers())
