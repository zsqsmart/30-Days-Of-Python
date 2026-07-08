a = 0
if a > 0:
    print('A是一个正数')
elif a < 0:
    print('A是一个负数')
else:
    print('A是零')

a = 3
print('A 是正数') if a > 0 else print('A 是负数')

a = 0
if a > 0:
    if a % 2 == 0:
        print('A 是一个整数且为偶数')
    else:
        print('A 是一个整数且为奇数')
elif a == 0:
    print('A 是零')
else:
    print('A 是负数')

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')

# age = input('请输入你的年龄：')
# age = int(age)
# if age >= 18:
#     print('你已经成年了')
# else:
#     print('你未成年')

# my_age = 18
# if age == my_age:
#     print('我们年龄相同')
# elif age > my_age:
#     print('你比我大', age - my_age, '岁')
# else:
#     print(f'你比我小 {my_age - age} 岁')

# score = input('请输入你的分数：')
# score = int(score)

# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')

# m = input('请输入月份：')
# m = int(m)
# if m in [9, 10, 11]:
#     print('秋天')
# elif m in [12, 1, 2]:
#     print('冬天')
# elif m in [3, 4, 5]:
#     print('春天')
# elif m in [6, 7, 8]:
#     print('夏天')
# else:
#     print('请输入一个有效的月份')

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': '芬兰',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {'street': '太空街', 'zipcode': '02210'},
}

# 检查是否在字典中有 skills 键，如果有则打印 skills 列表中的中间技能。
skills = person.get('skills')
if isinstance(skills, list):
    print(skills[len(skills) // 2])
    print('Python' in skills)
    #  如果一个人的技能只有 JavaScript 和 React，打印('他是前端开发者')，如果一个人的技能有 Node、Python、MongoDB，打印('他是后端开发者')，如果一个人的技能有 React、Node 和 MongoDB，打印('他是全栈开发者')，否则打印'未知头衔' - 为获得更准确的结果，可以嵌套更多条件！
    skill_set = set(skills)
    if {'React', 'Node', 'MongoDB'} <= skill_set:
        print('他是全栈开发者')
    elif {'Node', 'Python', 'MongoDB'} <= skill_set:
        print('他是后端开发者')
    elif {'JavaScript', 'React'} <= skill_set:
        print('他是前端开发者')
    else:
        print('未知头衔')
else:
    print('没有技能')
