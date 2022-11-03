# map co diccionarios 

items = [
    {
        'product':'camisa',
        'price':100
    },          
    {
        'product': 'pantalones',
        'price':300,
    },
    {
        'product': 'pantalones 2',
        'price': 200
    }
]

prices = list(map(lambda item: item['price'],items))
print(prices)

def addTaxes(item):
    item['taxes'] = item['price']*0.16
    return item

newItems = list(map(addTaxes,items))
print(newItems)