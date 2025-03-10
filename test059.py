number1 = int(input('Type your first value: '))
number2 = int(input('Type your second value: '))
print('''[1] to addition
    [2] to times
    [3] to the largest number
    [4] newer number
    [5] terminete the program''')
yourchoice = int(input(':'))
while yourchoice != 5:
    if yourchoice == 1:
        print(number1 + number2)
    elif yourchoice == 2:
        print(number1 * number2)
    elif yourchoice == 3:
        if number1 > number2:
            print(number1)
        elif number2 > number1:
            print(number2)
    elif yourchoice == 4:
        number1 = int(input('Type your first value:'))
        number2 = int(input('Type your second valuer:'))
    print('''Type again [1] to addition
    [2] to times
    [3] to power
    [4] newer number
    [5] terminete the program''')
    yourchoice = int(input(':'))