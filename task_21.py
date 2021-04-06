import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')


sentence = 'Lorem ipsum sit, amet consectetur adipisicing elit. Accusamus non sed impedit totam consequatur neque sunt repudiandae'

arr = ['lorem', 'ipsum', 'consectetur', 'adipisicing']

wordArr = sentence.split()

for i in range(0, len(wordArr)):
    for j in range(0, len(arr)):
        if(wordArr[i].upper() == arr[j].upper()):
            wordArr[i] = '***'

print(' '.join(str(x) for x in wordArr))
