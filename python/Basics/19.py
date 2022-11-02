#Diccionarios: insercion y actualizacion
person = {
    'name': 'Alex',
    'lastname': 'Guido',
    'langs': ['Python','Javascript'],
    'age': 24
}

print(person)

person['name'] = 'Sofia'
person['age'] -=2
person['langs'].append('rust')
print(person)

del person['lastname']
person.pop('age')

print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())