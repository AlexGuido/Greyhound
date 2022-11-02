# parametros por defecto y multiples returns
def findVolume(length = 1, width = 1, depth = 1):
    return length * width * depth, width, 'hola'
result, width, text = findVolume(width = 10)
print(result)
print(width)
print(text)