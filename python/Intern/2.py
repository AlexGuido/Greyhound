# set CRUD

setCountries = {'Mex','Col','Bol'}

size = len(setCountries)
print(size)

print('Mex' in setCountries)
print('pe' in setCountries)

#add
setCountries.add('pe')
print(setCountries)

#update
setCountries.update({'Ar','Ecu','Ar'})
print(setCountries)

#remove 
setCountries.remove('Mex')
print(setCountries)
setCountries.remove('Ar')
print(setCountries)

setCountries.discard('arg')
print(setCountries)
setCountries.add('Arg')
print(setCountries)

#clear all
setCountries.clear()
print(setCountries)
print(len(setCountries))