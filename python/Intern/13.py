# map
numbers = [1,2,3,4,]
numbersV2 = []
for i in numbers:
    numbersV2.append(i * 2)
# map hace lo mismo que el code de arriba.
numbersV3 = list(map(lambda i: i*2, numbers))

print(numbers)
print(numbersV2)
print(numbersV3)

#iterar dos listas
numbers1 = [1,2,3,4]
numbers2 = [5,6,7]

print(numbers1)
print(numbers2)
result = list(map(lambda x,y: x + y, numbers1,numbers2))
print(result) 
