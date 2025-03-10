import random
lista = (' Rock','Paper','Scissor')
print('Choose 0 for Rock')
print('Choose 1 for Paper')
print('Choose 2 for Scissor')
userchoice = int(input('Type your choice: '))
computerchoice = random.randint(0,2)
print('The player choice is {} and computer {}'.format(lista[userchoice],lista[computerchoice]))
if computerchoice == 0:
    if userchoice == 0:
        print('Draw')
    elif userchoice == 2:
        print(' The user lost')
    elif userchoice == 1:
        print(' The user is the winner')
elif computerchoice == 1:
    if userchoice == 1:
        print('Draw')
    elif userchoice == 0:
        print('The user lost')
    elif userchoice == 2:
        print('The user is the winner')
elif computerchoice == 2:
    if userchoice == 2:
        print('Draw')
    elif userchoice == 1:
        print('The user lost')
    elif userchoice == 0:
        print('The user is the winner')
else:
    print('It not a valid option')

