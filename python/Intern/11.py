# Lambdas
def increment(x):
    return x + 1

incrementV2 = lambda x : x+1 

result = increment(10)
print(11)

result = incrementV2(20)
print(result)

fullName = lambda name, lastname: f"FullName is {name.title()}{lastname.title()}"
text = fullName("Alexander", "Guido")
print(text)
