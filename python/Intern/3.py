#operaciones con conjuntos
setA = {'Mex','Col','Bol'}
setB = {'Pe','Bol'}

#union 
setC =setA.union(setB) #union forma 1
print(setC)
print(setA | setB) #union forma 2

#interserccion
setC = setA.intersection(setB) #inter forma 1
print(setC)
print(setA & setB)#inter forma 2

#diferencia
setC = setA.difference(setB)#forma 1
print(setC)
print(setA - setB) #forma 2

#Diferencia simetrica
setC = setA.symmetric_difference(setB)
print(setC)
print(setA ^ setB )
