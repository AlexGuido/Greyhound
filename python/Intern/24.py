#Escribir en un archivo
with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('Nuevas cosas en este archivo\n')
    file.write('other line\n')
    file.write('another line\n')