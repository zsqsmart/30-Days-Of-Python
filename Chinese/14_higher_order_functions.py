from collections.abc import Callable


def sum_numbers(nums: list[int]):
    return sum(nums)


def add_ten():
    ten = 10

    def add(num: int):
        return num + ten

    return add


closure_result = add_ten()

print(closure_result(5))


# 普通函数
def greeting():
    return 'Welcome to Python'


def uppercase_decorator(function: Callable[[], str]) -> Callable[[], str]:
    def wrapper() -> str:
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


g = uppercase_decorator(greeting)


print(g())


# 第二个装饰器
def split_string_decorator(function: Callable[[], str]):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


@split_string_decorator
@uppercase_decorator
def greeting():
    return 'Welcome to Python'


print(greeting())


names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # 可迭代对象


def change_to_upper(name: str):
    return name.upper()


names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))

names_upper_cased: map[str] = map(lambda name: name.upper(), names)
print(list(names_upper_cased))
