price = int(input('The value of your purchases: '))
print('Press [1] for cash purchases' )
print('Press [2] for debt card purchases ')
print('Press [3] for credit card purchases (2x) ')
print('Press [4] for credit card purchases (3x or more) ')
waytopay = int(input('Type here: '))
if waytopay == 1:
    print(price - (price*0.10))
elif waytopay == 2:
    print( price - (price*0.05))
elif waytopay == 3:
    print('it will be {}'.format( price / 2))
elif waytopay == 4:
        install = int(input('How many installements? '))
        print('The value will be {}'.format( price + (price * 20 / 100)))
else:
    print('It not a valid option!')




