import random
randoint = random.randint(0,10)
yournumber =(int(input('I´m your computer. Can you guess which number from 0 to 10 i choose? ')))
misses = 0
while yournumber != randoint:
    if yournumber < randoint:
        print('Your number is less than the computer´s')
        misses += 1
    elif yournumber > randoint:
        misses += 1
        print('Your number is bigger than computer´s')
    yournumber = int(input('Type again you missed: '))
print(f'The computer number is {randoint} and you missed {misses} times')


