number = int(input('Type a number: '))
xs = 0
for c in range(1, number+1, 1):
    if number % c == 0:
        print('The number is divided by {}'.format(c),)
        xs +=1
    else:
        print("not divided by {}".format(c))
print(f'The number is divided {xs} times')
if xs > 2:
    print('Não é um número primo')
else:
    print('é um número primo' )