rn = int(input('Type the first number: '))
ra = int(input('Digite a razão: '))
c = 0
r = rn
while c < 10:
    r += ra
    print(f'{r} ->',end= ' ')
    c += 1
n = str(input('Want more [Y/N] ')).upper().strip()
if n =='Y':
    c = 0
    g = int(input('how many: '))
    while c < g :
        r += ra
        print(f'{r} ->', end=' ')
        c += 1
else:
    print('end')