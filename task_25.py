import random
import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')

suits = ["s", "d", "c", "h"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

coloda = []
for i in range(0, len(suits)):
    for j in range(0, len(values)):
        card = values[j] + suits[i]
        coloda.append(card)


def shuffle(coloda):
    lastIndex = len(coloda)-1
    while lastIndex > 0:
        randomIndex = random.randint(0, lastIndex)
        last = coloda[lastIndex]
        coloda[lastIndex] = coloda[randomIndex]
        coloda[randomIndex] = last
        lastIndex -= 1


print('Не тасована колода: ', coloda)
shuffle(coloda)
print('Перетасована колода: ', coloda)
