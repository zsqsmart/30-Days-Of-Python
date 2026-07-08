import json
from collections import Counter
from pathlib import Path
from typing import TypedDict, cast


class Country(TypedDict):
    name: str
    capital: str
    languages: list[str]
    population: int
    flag: str
    currency: str


count = 0
while count < 5:
    count += 1
    if count == 2:
        continue
    print(count)
    if count == 3:
        break
else:
    print('count值不再小于5')

for number in range(1, 11):
    print(number)
for letter in 'Python':
    print(letter)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {'street': 'Space street', 'zipcode': '02210'},
}

for key, value in person.items():
    print(key, value)
    if key == 'skills' and isinstance(value, list):
        for skill in value:
            print(skill)
else:
    print('loop end')

for number in range(10, -1, -1):
    print(number)

for number in range(1, 7):
    print('#' * number)

for number in range(1, 7):
    print('# ' * 7)

ls = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in ls:
    if 'P' in item:
        print(item)
for number in range(1, 101):
    if number % 2 == 0:
        print(number)

total = 0
for number in range(1, 101):
    total += number
print(f'The sum of all numbers is {total}.')

odd_total = 0
even_total = 0
for number in range(1, 101):
    if number % 2 == 1:
        odd_total += number
    else:
        even_total += number
print(f'The sum of all odd numbers is {odd_total}. The sum of all even numbers is {even_total}.')

# 使用循环反转列表中的元素
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits: list[str] = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
print(reversed_fruits)


data_path = Path(__file__).resolve().parent.parent / 'data' / 'countries_data.json'

with open(data_path, encoding='utf-8') as f:
    countries_data = cast(list[Country], json.load(f))

language_counter = Counter(
    language for country in countries_data for language in country['languages']
)
# 数据中一共有多少个语言？
print(f'数据中一共有{len(language_counter)}种语言')
# 找到被最多国家使用的语言。
print(language_counter.most_common(1))
# 找到人数排名前十的国家。

top10_countries = sorted(countries_data, key=lambda c: c['population'], reverse=True)[:10]
for country in top10_countries:
    print(country['name'], country['population'])
