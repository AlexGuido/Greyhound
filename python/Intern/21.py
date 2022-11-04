# errores
#print(0/0)
#print(result)
suma = lambda x,y: x + y
assert suma(3,4) == 7

x = 10
if x < 18:
    raise Exception('No se permiten menores de edad')  