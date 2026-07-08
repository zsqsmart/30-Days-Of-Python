import math


def add_two_numbers(num1: int, num2: int):
    return num1 + num2


print(add_two_numbers(1, 2))


def area_of_circle(r: float):
    return math.pi * r**2


print(area_of_circle(2.3))


def add_all_nums(*args: int):
    total = sum(args)
    return total


print(add_all_nums(1, 2, 3, 4, 5))


def convert_celsius_to_fahrenheit(c: float):
    return (c * 9 / 5) + 32


print(convert_celsius_to_fahrenheit(37))


def check_season(m: int):
    if m in [9, 10, 11]:
        return '秋天'
    elif m in [12, 1, 2]:
        return '冬天'
    elif m in [3, 4, 5]:
        return '春天'
    elif m in [6, 7, 8]:
        return '夏天'
    else:
        return '月份错误'


print(check_season(1))


def calculate_slope(x1: float, y1: float, x2: float, y2: float):
    return (y2 - y1) / (x2 - x1)


print(calculate_slope(1, 2, 3, 4))


# 二次方程按以下公式计算：ax² + bx + c = 0。编写一个函数计算二次方程的解集，solve_quadratic_eqn。
def solve_quadratic_eqn(a: float, b: float, c: float):
    delta: float = b**2 - 4 * a * c
    if delta < 0:
        return '无实数解'
    elif delta == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2


print(solve_quadratic_eqn(1, 2, 3))


def print_list(ls: list[str | int]):
    for item in ls:
        print(item)


print_list([1, 2, 3, 4, 5, 'a', 'b', 'c'])


def reverse_list(ls: list[str | int]):
    reversed_list: list[str | int] = []
    for i in range(len(ls) - 1, -1, -1):
        reversed_list.append(ls[i])
    return reversed_list


print(reverse_list([1, 2, 3, 4, 5]))


def capitalize_list_items(ls: list[str]):
    result: list[str] = []
    for item in ls:
        result.append(item.capitalize())
    return result


print(capitalize_list_items(['a', 'b', 'c', 'd', 'e']))


def add_item(ls: list[str], item: str):
    ls.append(item)
    return ls


print(add_item(ls=['a', 'b', 'c', 'd', 'e'], item='f'))


def remove_item(ls: list[str], item: str):
    ls.remove(item)
    return ls


print(remove_item(ls=['a', 'b', 'c', 'd', 'e'], item='a'))


def sum_of_numbers(num: int):
    return sum(range(1, num + 1))


print(sum_of_numbers(num=100))


# 声明一个名为 sum_of_odds 的函数。它接受一个数字参数并将范围内的所有奇数相加。
def sum_of_odds(num: int):
    total = 0
    for i in range(1, num + 1):
        if i % 2 != 0:
            total += i
    return total


print(sum_of_odds(num=100))


# 声明一个名为 sum_of_even 的函数。它接受一个数字参数并将范围内的所有偶数相加。
def sum_of_even(num: int):
    total = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            total += i
    return total


print(sum_of_even(num=100))


def evens_and_odds(num: int):
    odds = 0
    evens = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return {'odds': odds, 'evens': evens}


result = evens_and_odds(num=100)
print(result['odds'], result['evens'])
print(evens_and_odds(num=100))


def is_prime(num: int):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
