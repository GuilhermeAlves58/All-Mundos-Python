plus = 0
cont = 0
for impar in range(1,501, +2):
    if impar % 3 == 0:
        cont = cont + 1
        plus = plus + impar
print('{} e {} '.format(plus, cont))