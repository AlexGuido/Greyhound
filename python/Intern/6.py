# Dictionary Comprehension: Condition
import random
countries =['col','mex','bol','pe'] 

populationV2 = {i: random.randint(1,100) for i in countries}
print(populationV2)

result = {i: j for (i,j) in populationV2.items()if j > 20}
print(result)

text = 'Hola, soy Mozzi'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print(unique)