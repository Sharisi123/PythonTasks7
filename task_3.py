import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')

off = False
uniqueValues = set()

while off != True:
    word = input('Введіть значення: ')
    if(word == ''):
        off = True
        break
    uniqueValues.add(word)

for value in uniqueValues:
    print(value)
