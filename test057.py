sexo = str(input('Type your sex [M/F]: ')).upper().strip()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Type your sex [M/F]: ')).upper()
print(f'{sexo} wrote down')