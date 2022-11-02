# list comprehension
'''
numbers = []
for i in range(1,11):
    numbers.append(i * 2)
print(numbers)

numbersV2 = [i*2 for i in range(1,11)]
print(numbersV2)
'''
numbers = []
for i in range(1,11):
    if i % 2 == 0:
        numbers.append(i*2)
print(numbers)

numbersV2 = [i*2 for i in range(1,11) if i%2 == 0]
print(numbersV2)


