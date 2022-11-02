# for 
'''
for element in range(1,21):
    print(element)

'''
myList = [23,45,67,89,43]
for i in myList:
    print(i)

myTuple = ('Alex','Guido','Denis')
for i in myTuple:
    print(i)

product = {
    'name':'camisa',
    'price':100,
    'stock':89
}
for i in product:
    print(i,'=>',product[i])

print('-'*10)
for key, value in product.items():
    print(key,'=>',value) 
print('-'*10)
people = [
    {
        'name': 'Alex',
        'age': '25'
    },
    {
        'name': 'paola',
        'age': 50
    },
    {
        'name': 'Andy',
        'age':23
    }
]

for i in people:
    print('name =>',i['name'])