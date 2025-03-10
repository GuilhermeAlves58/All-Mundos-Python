n1 = int(input('Type a number '))
n2 = int(input('Type a number '))
n3 = int(input('Type a number '))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
if maior > menor:
    print('largest number is {}'.format(maior))
    print('smallest number is {}'.format(menor))
else:
    print('the value is the same')
