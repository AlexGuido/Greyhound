# Funciones: return
def sumWithRange(min, max):
    print(min,max)
    sum = 0
    for i in range(min,max):
        sum +=i
    return sum

result = sumWithRange(100000,3000000)
print(result)
result2 = sumWithRange(result,result + 10)
print(result2)