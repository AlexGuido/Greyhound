# metodos de listas
# CRUD Create, Read, update, Delete

numbers = [1,2,3,4,5] #create
print(numbers[1])   # Read
numbers[-1] = 10    #update
print(numbers) 

numbers.append(700)
print(numbers)

numbers.insert(0,'hello')
print(numbers)

numbers.insert(3,'change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo3']
newList = numbers + tasks
print(newList)

index = newList.index('todo 2')
newList[index] = 'todo change'
print(newList)

newList.remove('todo 1')
print(newList)

newList.pop()
print(newList)

newList.pop(0)
print(newList)

newList.reverse()
print(newList)

numbersA = [1,4,6,3]
numbersA.sort()
print(numbersA)

strings = ['re','ab','ed']
strings.sort()
print(strings)