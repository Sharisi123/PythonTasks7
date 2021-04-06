import random
import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')

balance = 100
things = ['Cherry', 'Bell', 'Lemon', 'Orange', 'Star', 'Skull']
answer = input('Почати гру? 1- Так 2- Ні: ')

while answer == '1':
    balance -= 5
    first = things[round(random.random()*5)]
    second = things[round(random.random()*5)]
    third = things[round(random.random()*5)]
    print('\n', first, second, third, sep='\n', end='\n')
    if(first == second == third):
        if(first == 'Bell'):
            print('Вітаю! Ви виграли 100 грн!\n')
            balance += 100
            print('Ваш баланс: ', balance)
            answer = input('Продовжити гру? 1- Так 2- Ні: ')
        elif(first == 'Skull'):
            print('Cпівчуваю! Ви витратили 100 грн!\n')
            balance -= 100
            print('Ваш баланс: ', balance)
            answer = input('Продовжити гру? 1- Так 2- Ні: ')
        else:
            print('Вітаю! Ви виграли 25 грн!\n')
            balance += 25
            print('Ваш баланс: ', balance)
            answer = input('Продовжити гру? 1- Так 2- Ні: ')

    if(first == second or first == third or second == third):
        if(first == 'Skull' or second == 'Skull'):
            print('Cпівчуваю! Ви витратили 5 грн!\n')
            balance -= 5
            print('Ваш баланс: ', balance)
            answer = input('Продовжити гру? 1- Так 2- Ні: ')
        else:
            print('Вітаю! Ви виграли 10 грн!\n')
            balance += 10
            print('Ваш баланс: ', balance)
            answer = input('Продовжити гру? 1- Так 2- Ні: ')
    else:
        print('Нічого не випало')
        print('Ваш баланс: ', balance)
        answer = input('Продовжити гру? 1- Так 2- Ні: ')
