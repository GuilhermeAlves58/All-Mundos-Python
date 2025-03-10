soma = 0
for c in range(1,7):
    numberss = int(input('Type a number: '))
    if numberss % 2 == 0:
       soma = soma + numberss
print(soma)