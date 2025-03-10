from random import randint
c = 0
while True:
    computers = randint(0,100)
    playesint= int(input('Digite um numero [0/100]: '))
    playesstr= str(input('Type [I/P]: ')).strip().upper()
    total = computers + playesint
    if playesstr not in 'IP':
        while playesstr not in 'IP':
            playesstr= str(input('Type [I/P]: ')).strip().upper()
    if playesstr == 'I' and total % 2 != 0 :
        print(f'The player won {total} and computer´s  {computers} ')
        c += 1
    elif playesstr == 'P' and total % 2 == 0:
        print(f'The player won {total} and computer´s  {computers}')
        c += 1
    else:
        print(f'the computer won {total} and computer´s {computers}')
        print(f'total number of wins {c}')
        break
    print('')