# Transformacion de tipos
name = "Alex"
print(type(name))
name = 12
print(type(name))
name = True 
print(type(name))

print("Alex" + "Guido")
print(10 + 20)
print("Alex" + "12")

age = 12
print(f"mi edad es {age}")
#print("Mi edad es " + str(age))

age = input("Escribe tu edad: ")
print(type(age))
age = int(age)
print(f"Tu edad en 10 años sera {age + 10}")