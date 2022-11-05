import utils 
import read
import charts

def run():
    data = read.readCSV('data.csv') 
    country = input('Type Country: ')

    result = utils.populationByCountry(data,country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.getPopulation(country)
        charts.generateBarChart(labels,values)

if __name__ == '__main__':
    run()