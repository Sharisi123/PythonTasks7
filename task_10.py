import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')

balance = 100

things = [u"\U0001F352", u"\U0001F514",
          u"\U0001F34B", u"\U0001F34A", u"\u2606", u"\U0001F480"]

for t in things:
    print(t)
