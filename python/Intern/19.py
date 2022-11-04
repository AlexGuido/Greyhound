#modulos
import sys
print(sys.path)

import re 
text = 'Mi numero de telefono es 555555, el codigo del pais es 52, mi numero de la suerte es 3'
result = re.findall('[0-9]+',text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(result)

import collections
numbers = [1,2,1,3,4,5,6,5,2,3,4,6,7]
counter = collections.Counter(numbers)
print(counter)