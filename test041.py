from datetime import date
currentyear = date.today().year
birthyear= int(input('Type your birthyear: '))
classification= currentyear - birthyear
if classification <= 9:
    print('Mirin')
elif classification <= 14:
    print('child')
elif classification <= 19:
    print('junior')
elif classification <= 25:
    print('Senior')
else:
    print('Master ')
