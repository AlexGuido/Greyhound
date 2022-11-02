# Dictionary Comprehension
import random
'''
dict = {}
for i in range(1,5):
    dict[i] = i*2
print(dict)

dictV2 = {i:i*2 for i in range(1,5)}
print(dictV2)

countries = ['col','mex','bol','pe']
population = {}
for i in countries:
    population[i] = random.randint(1,100)
print(population)

populationV2 ={i: random.randint(1,100) for i in countries}
print(populationV2)
'''
names = ['Alex', 'Guido', 'Denis']
age = [24,25,17]

print(list(zip(names, age)))

newDict = {name:age for (name, age) in zip(names, age)}
print(newDict)