import utils 

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

def run(): 
    keys, values = utils.getPopulation()
    print(keys,values)
    country = input('Type Country: ')
    result = utils.populationByCountry(data,country)
    print(result)

if __name__ == '__main__':
    run()