import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')

letters = {
    'A': 1,
    'E': 1,
    'I': 1,
    'L': 1,
    'N': 1,
    'O': 1,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'D': 2,
    'G': 2,
    'B': 3,
    'C': 3,
    'M': 3,
    'P': 3,
    'F': 4,
    'H': 4,
    'V': 4,
    'W': 4,
    'Y': 4,
    'K': 5,
    'J': 8,
    'X': 8,
    'Q': 10,
    'Z': 10,
}
accum = 0

word = input('Введіть слово для гри: ')
word = word.upper()
for i in range(0, len(word)):
    for key in letters:
        if(word[i] == key):
            accum += letters[key]

print('Ваша кількість балів за слово: ', accum)
