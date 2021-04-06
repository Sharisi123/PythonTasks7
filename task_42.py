import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')


arr = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
print(f'-------')
print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
i = 1
j = 0
off = False


while off != True:
    row = input('Введіть рядок: ')
    column = input('Введіть колонку: ')

    if(row == '1'):
        if(column == '1'):
            if(arr[0] == ' '):
                if(i % 2 == 0):
                    arr[0] = 'O'
                    i += 1
                else:
                    arr[0] = 'X'
                    i += 1
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
            else:
                print('Зайнято')
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
        if(column == '2'):
            if(arr[1] == ' '):
                if(i % 2 == 0):
                    arr[1] = 'O'
                    i += 1
                else:
                    arr[1] = 'X'
                    i += 1
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
            else:
                print('Зайнято')
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
        if(column == '3'):
            if(arr[2] == ' '):
                if(i % 2 == 0):
                    arr[2] = 'O'
                    i += 1
                else:
                    arr[2] = 'X'
                    i += 1
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
            else:
                print('Зайнято')
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')

    if(row == '2'):
        if(column == '1'):
            if(arr[3] == ' '):
                if(i % 2 == 0):
                    arr[3] = 'O'
                    i += 1
                else:
                    arr[3] = 'X'
                    i += 1
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
            else:
                print('Зайнято')
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
        if(column == '2'):
            if(arr[4] == ' '):
                if(i % 2 == 0):
                    arr[4] = 'O'
                    i += 1
                else:
                    arr[4] = 'X'
                    i += 1
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
            else:
                print('Зайнято')
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
        if(column == '3'):
            if(arr[5] == ' '):
                if(i % 2 == 0):
                    arr[5] = 'O'
                    i += 1
                else:
                    arr[5] = 'X'
                    i += 1
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
            else:
                print('Зайнято')
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')

    if(row == '3'):
        if(column == '1'):
            if(arr[6] == ' '):
                if(i % 2 == 0):
                    arr[6] = 'O'
                    i += 1
                else:
                    arr[6] = 'X'
                    i += 1
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
            else:
                print('Зайнято')
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
        if(column == '2'):
            if(arr[7] == ' '):
                if(i % 2 == 0):
                    arr[7] = 'O'
                    i += 1
                else:
                    arr[7] = 'X'
                    i += 1
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
            else:
                print('Зайнято')
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
        if(column == '3'):
            if(arr[8] == ' '):
                if(i % 2 == 0):
                    arr[8] = 'O'
                    i += 1
                else:
                    arr[8] = 'X'
                    i += 1
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')
            else:
                print('Зайнято')
                print(f'|{arr[0]}|{arr[1]}|{arr[2]}|')
                print(f'|{arr[3]}|{arr[4]}|{arr[5]}|')
                print(f'|{arr[6]}|{arr[7]}|{arr[8]}|')

    if(arr[0] == 'X' and arr[1] == 'X' and arr[2] == 'X'):
        print('Виграли Х!')
        break
    if(arr[3] == 'X' and arr[4] == 'X' and arr[5] == 'X'):
        print('Виграли Х!')
        break
    if(arr[6] == 'X' and arr[7] == 'X' and arr[8] == 'X'):
        print('Виграли Х!')
        break
    if(arr[0] == 'X' and arr[3] == 'X' and arr[6] == 'X'):
        print('Виграли Х!')
        break
    if(arr[1] == 'X' and arr[4] == 'X' and arr[7] == 'X'):
        print('Виграли Х!')
        break
    if(arr[2] == 'X' and arr[5] == 'X' and arr[8] == 'X'):
        print('Виграли Х!')
        break
    if(arr[0] == 'X' and arr[4] == 'X' and arr[8] == 'X'):
        print('Виграли Х!')
        break
    if(arr[2] == 'X' and arr[4] == 'X' and arr[6] == 'X'):
        print('Виграли Х!')
        break

    if(arr[0] == 'O' and arr[1] == 'O' and arr[2] == 'O'):
        print('Виграли О!')
        break
    if(arr[3] == 'O' and arr[4] == 'O' and arr[5] == 'O'):
        print('Виграли О!')
        break
    if(arr[6] == 'O' and arr[7] == 'O' and arr[8] == 'O'):
        print('Виграли О!')
        break
    if(arr[0] == 'O' and arr[3] == 'O' and arr[6] == 'O'):
        print('Виграли О!')
        break
    if(arr[1] == 'O' and arr[4] == 'O' and arr[7] == 'O'):
        print('Виграли О!')
        break
    if(arr[2] == 'O' and arr[5] == 'O' and arr[8] == 'O'):
        print('Виграли О!')
        break
    if(arr[0] == 'O' and arr[4] == 'O' and arr[8] == 'O'):
        print('Виграли О!')
        break
    if(arr[2] == 'O' and arr[4] == 'O' and arr[6] == 'O'):
        print('Виграли О!')
        break

    for el in arr:
        if(el != ' '):
            j += 1
    if(j == 45):
        print('Нічия')
        break
