#Модули
#1 - импортировать сам модуль
# import lesson_8

# lesson_8.welcome('Bayastan')
# lesson_8.add(100, 34)

#2
from lesson_8 import welcome, add

welcome('Beksultan')
add(200, 1234)

#3
from lesson_8 import *

welcome('Nurbolot')
add(333, 345)