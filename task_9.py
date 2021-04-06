import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')

print('Натисніть 1 для першого класу(місця 1-6)')
print('Натисніть 2 для економного класу(місця 7-12).')

isSitFree = [False, False, True, False, True, False,
             False, False, False, False, False, False]

sit = input('Ваша цифра: ')

if(sit == '1'):
    print('Дякуємо за обрання першого класу')
    for i in range(0, 6):
        if(isSitFree[i]):
            print('Ваше місце під номером ', i+1)
            break
else:
    print('Дякуємо за обрання eконом класу')
    for i in range(6, 13):
        if(isSitFree[i]):
            print('Ваше місце під номером ', i+1)
            break
        else:
            print(
                'Усі місця в економ класі зайняті, чи не хочете придбати квиток першого класу?\n 1 - Taк 2 - Ні')
            suggestion = input('Ваша цифра: ')
            if(suggestion == '1'):
                print('Дякуємо за обрання першого класу')
                for i in range(0, 6):
                    if(isSitFree[i]):
                        print('Ваше місце під номером ', i+1)
                        break
                break
            else:
                print('Наступний літак через 3 години')
                break
