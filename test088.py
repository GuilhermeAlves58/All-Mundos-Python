from random import randint
number_games = int(input('Type how many games do you want: '))
listvalues = []
games = listvalues
c = x = 0
while True:
    while x < 6:
        lucknum = randint(1,60)
        if lucknum not in listvalues:
            listvalues.append(lucknum)
            x += 1
    x = 0
    c += 1
    games.append(listvalues)
    print(f'{c} try {games}')
    listvalues.clear()
    if c == number_games:
        break
