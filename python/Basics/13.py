# String recargado
text = 'Ella sabe programar en python'
'''
print('JavaScript' in text)
print('python' in text)

if 'js' in text:
    print('Elegiste bien')
else:
    print('Tambien elegiste bien')
'''
size = len(text)
print(size)
print(text)
print(text.upper())
print(text.lower())
print(text.count('a'))#contar el caracter 'a' en el texto
print(text.swapcase())# mayus a minus y viceversa

print(text.startswith('Ella'))
print(text.endswith('Rust'))
print(text.replace('python', 'Go'))

text2 = 'este es un titulo'
print(text2)
print(text2.capitalize())
print(text2.title())
print(text2.isdigit())
print('43'.isdigit())