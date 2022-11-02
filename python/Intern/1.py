# set
# Los caracteres no se repiten
setCountries = {'col','mex','bol'}
print(type(setCountries))

setNumbers = {1,2,3,3,44,55}
print(setNumbers)

setTypes = {1,'hola',False,12.22}
print(setTypes)

setFromString = set('hoola')
print(setFromString)

setFromTuple = set(('abc','cbv','as','abc'))
print(setFromTuple)

numbers = [1,2,3,1,2,3,4]
setNumbers = set(numbers)
print(setNumbers)
uniqueNumbers = list(setNumbers)
print(uniqueNumbers)