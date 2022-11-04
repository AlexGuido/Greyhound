def getPopulation():
    keys = ['Col','Bol']
    values = [300, 400]
    return keys, values

def populationByCountry(data, country):
    result = list(filter(lambda x:x['Country']== country,data))
    return result

