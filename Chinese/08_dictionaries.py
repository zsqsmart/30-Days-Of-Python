empty_dict = {}

dct = {'key1': 'value1', 'key2': 'value2'}

person = {'first_name': 'Asabeneh', 'last_name': 'Yetayeh', 'age': 250}

print(person)
print(len(person))
print(person['first_name'])
print(person['last_name'])
print(person.get('city'))  # 错误
print('age' in person)
print({'a': 1, 'b': [1, 2]} == {'b': [1, 2], 'a': 1})

dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

print(dct.items())
print('keys', dct.keys())
print('values', dct.values())

dct.clear()

print('cleared', dct)

dog = {}
dog['name'] = 'Buddy'
dog['age'] = 3
dog['color'] = 'brown'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['tail'] = True
dog['ears'] = True
dog['eyes'] = True
dog['nose'] = True
dog['mouth'] = True
dog['paws'] = True
dog['tail'] = True

print(dog)

student = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'city': 'Helsinki',
    'skills': ['Python', 'JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {'street': 'Space street', 'zipcode': '02210'},
}

print(student)
print(len(student))
student.pop('first_name')
print(student)

for key in list(student.keys()):
    value = student[key]
    if isinstance(value, dict):
        student.pop(key)
print(student)
