import utils 

keys, values = utils.getPopulation()
print(keys,values)

data = [
    {
        'Country':'Colombia',
        'Population':300
    },
    {
        'Country':'Bolivia',
        'Population':300
    }
]

country = input('Tyoe Country: ')

result = utils.populationByCountry(data,country)
print(result)