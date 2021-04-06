import random

import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')

first = ['Apple', 'Mouse', 'Milk', 'Juice', 'Fruit']
second = ['House', 'Bear', 'Lamp', 'Frige', 'Force']

word = ''
word += first[round(random.random()*4)] + second[round(random.random()*4)]
if(len(word) < 8 or len(word) > 10):
    print('Не підходить')
else:
    print(word)
