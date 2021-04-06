import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')


def caprecarNumber(num):
    square = num * num
    numStr = str(square)
    if(len(str(num)) % 2 != 0):
        print('Працюю тільки з парними числами')
        return -1
    firstPart = numStr[0:2]
    secondPart = numStr[2:]
    if(int(firstPart) + int(secondPart) == num):
        print('Це число капрекара')
        print(firstPart, secondPart)
    else:
        print('Число не є числом капрекара')
        return -1


num = input('Введіть число: ')
caprecarNumber(int(num))
