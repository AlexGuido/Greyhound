#string
name = "Alexander"
lastname = "Guido"
print(name)
print(lastname)

#concatenacion
full_name = name +' '+lastname
print(full_name)

quote = "I'm AlexGuido"
print(quote)
quote2 = 'She said "Hello" ji ji '
print(quote2)

# format
template = "Hola, mi nombre es: " + name + " y mi apellidoes "+ lastname
print("v1: ",template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, lastname)
print("v2: ",template)

template = f"Hi, my name is {name} and my lastname is: {lastname}"
print("v3: ",template)