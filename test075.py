tupla = (int(input('Type a number: ')),int(input('Type a number: ')),int(input('Type a number: ')),
int(input('Type a number: ')))
print(tupla)
if 3 in tupla:
    print(f'The number three Appears {tupla.index(3) + 1} position')
if 9 in tupla:
    print(f'{tupla.count(9)} times')
for n in tupla:
    if n % 2 == 0:
        print(f'The values {n}',end=' ')