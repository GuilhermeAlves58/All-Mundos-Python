from datetime import date
Birthday= int(input('Type your birthday '))
if (date.today().year - Birthday) > 18:
    print('{} passed and The Army calls you'.format((date.today().year - Birthday) - 18))
elif (date.today().year - Birthday) < 18:
    print('You are too young, needs {} years'.format( Birthday- date.today().year + 18))
elif (date.today().year - Birthday) == 18:
    print('you are in the exact age')

