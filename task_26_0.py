import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp('Наживотов Олександр')

shuffledCards = ['3s', 'Js', '4s', '5h', 'Ac', 'Qh', '4d', 'Qs', '2s', 'Jc', 'Ad', 'Kh', '7d', '3c', '5c', '6d', 'Jh', 'Kd', '7h', '8c', '8h', 'Qd', '7s', 'Kc', 'Jd',
                 '8d', '4h', '5d', '6h', 'Td', '3h', '6c', '9h', 'Ks', '4c', 'Th', '2h', '5s', 'Qc', 'Tc', '9s', '6s', '7c', '2d', 'Ts', '8s', 'Ah', '3d', '9d', '2c', 'As', '9c']


def cardDispenser(shuffledCards):
    countOfPeople = input('Введіть кількість гравців: ')
    countOfCardPerPlayer = input('Введіть кількість карт на одного гравця: ')
    playerCards = []

    if(int(countOfPeople) * int(countOfCardPerPlayer) > len(shuffledCards)):
        print('Карт на всіх не вистачить')
        return 0

    for i in range(0, int(countOfPeople)):
        playerCards = []
        for j in range(0, int(countOfCardPerPlayer)):
            playerCards.append(shuffledCards[j])
            shuffledCards.remove(shuffledCards[j])
        print('Карти гравця номер: ', i+1)
        print(playerCards)


cardDispenser(shuffledCards)
