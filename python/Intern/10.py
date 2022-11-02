price = 100 #Global
result = 200

def increment():
    price = 200 #local
    result = price + 10
    print(result)
    return result

print(price)
price2 = increment()
print(price2)
