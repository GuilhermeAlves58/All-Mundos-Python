lista = []
fivecheck = False
lista.append(int(input('Type a value: ')))
while True:
    ifnot = str(input('Want to continue? [Y/N]')).upper().strip()
    if 'N' in ifnot:
        break
    elif 'Y' in ifnot:
        lista.append(int(input('Type a value: ')))
        if 5 in lista:
            fivecheck = True
    else:
        print('Type [y/n]')
org = sorted(lista,reverse= True)
print(f'Lenght of the list {len(lista)} itens')
print(f' the numbers in a decreasing way [{org}]')
if fivecheck == True:
    print(f'The value 5 is in the list')
else:
    print(f'The value 5 is not in the list')