lista = []
c = 0
while True:
    num1 = (int(input("Type a number: ")))
    num = (int(input("Type other number: ")))
    lista.append(num1)
    lista.append(num)
    c += 1
    if num1 == num:
        print('Same number! Please type other number: ')
        del lista[c]
    startedn = str(input('Want to continue?[Y/N] ')).upper().strip()
    if 'N' in startedn:
        break
print(f'{sorted(lista)}')