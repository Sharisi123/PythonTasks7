import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')


accum = 0
arr = []
off = False
i = 0

while off != True:
    num = input('Введіть число:')
    if(num == ''):
        avarage = accum / len(arr)
        print('Середнє число: ', avarage)
        print('Числа більні за середнє: ')
        for num in arr:
            if(num >= avarage):
                print(num)
        print('Числа менші за середнє: ')
        for num in arr:
            if(num < avarage):
                print(num)
        off = True
        break
    accum += int(num)
    arr.append(int(num))
