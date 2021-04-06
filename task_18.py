import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')


card = '4578423013769219'


def cardCheaker(card):
    accum = 0
    for i in range(0, len(card)):
        if(i % 2 == 0):
            double = int(card[i]) * 2
            if(len(str(double)) == 2):
                doubleStr = str(double)
                double = int(doubleStr[0]) + int(doubleStr[1])
                accum += double
            else:
                accum += double

        else:
            accum += int(card[i])

    if(accum % 10 == 0):
        print('Correct!')
        print(accum)
    else:
        print('Error')
        print(accum)


cardCheaker(card)
