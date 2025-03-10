listab = []
listacp = []
listadi = []
num = int(input('Type a number: '))
listab.append(num)
while True:
    conti = str(input('Want to continue:[Y/N] ')).upper().strip()
    if 'N' in conti:
        break
    elif 'Y' in conti:
        num = int(input('Type a number: '))
        listab.append(num)
        if num % 2 == 0:
            listacp.append(num)

        else:
            listadi.append(num)
    else:
        print('Type [Y/N]')
print(f'The intire list {listab}')
print(f'Pair: {listacp}')
print(f'impar: {listadi}')
