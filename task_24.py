import winsound
import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')


arr = [[440, 500], [440, 500], [440, 500], [349, 350], [523, 150], [440, 500], [349, 350], [523, 150],
       [440, 1000], [659, 500], [659, 500], [659,
                                             500], [698, 350], [523, 150], [415, 500], [349, 350],
       [523, 150], [440, 1000]]

for music in arr:
    winsound.Beep(music[0], music[1])
