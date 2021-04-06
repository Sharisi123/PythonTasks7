import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = input('Введіть число n: ')

if(int(n)+1 > round(len(arr) / 2)):
    print('Помилка: при введенні даного числа, список буде пустим.')

else:
    for i in range(0, int(n)):
        arr.sort()
        del arr[0]
        del arr[-1]

print(arr)
