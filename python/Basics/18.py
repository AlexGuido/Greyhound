#diccionario
myDict = {}
print(type(myDict))

myDict = {
    'avion': 'bla bla bla',
    'name': 'Alexander',
    'lastname': 'Guido',
    'age': 25
}

print(myDict)
print(len(myDict))

print(myDict['age'])
print(myDict['lastname'])
print(myDict.get('age'))#para saber si existe una llave en el dict

print('avion' in myDict)
print('other' in myDict)
