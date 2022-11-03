# Higher order function: una funcion dentro de otra funcion
def increment(x):
    return x+1

incrementV2 = lambda x : x+1


def higherOrderFunc(x,func):
    return x + func(x)

higherOrderFuncV2 = lambda x,func: x+ func(x)
result = higherOrderFunc(2,increment)
print(result)

result	= higherOrderFuncV2(2,incrementV2)
print(result)

result = higherOrderFuncV2(2,lambda x: x+2)
print(result)
result = higherOrderFuncV2(2, lambda x:x*2)
print(result)