#tuplas
# no se pueden hacer cambios en ellas

numbers = (1,2,3,5)
strings = ('nico', 'mateo', 'sofi','nico','nico')
print(numbers)
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

print(strings.index('sofi'))
print(strings.count('nico'))

myList = list(strings)
print(myList)
print(type(myList))

myList[0] = 'Alexander'
print(myList)
myTupla = tuple(myList)
print(myTupla)
print(type(myTupla))