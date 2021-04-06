import random
import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')


article = ['The', 'A', 'One', 'Some', 'Any']
noun = ['boy', 'girl', 'dog', 'town', 'car']
verb = ['drove', 'jumped', 'ran', 'walked', 'skipped']
preposition = ['to', 'from', 'over', 'under', 'on']


for i in range(0, 10):
    print(str(i+1) + '.', article[round(random.random()*4)], noun[round(random.random()*4)],
          verb[round(random.random()*4)],
          preposition[round(random.random()*4)], sep=' ', end='.\n')
