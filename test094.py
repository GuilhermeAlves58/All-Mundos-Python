dictonary = {}
fcount = []
lista = [[],[]]
count = c = 0

while True:
    dictonary['name'] = str(input('Name: ')).strip().capitalize()
    dictonary['age'] = int(input('Age: '))
    dictonary['sex'] = str(input('sex[M/F]: ')).upper().strip()
    lista[1].append(dictonary['age'])
    count += 1
    if dictonary['sex'] == 'F':
        fcount.append(dictonary['name'])
    conti = str(input('continue[Y/N]: ')).upper().strip()
    if conti != 'Y':
        conti = str(input('continue[Y/N]: ')).upper().strip()
    if conti == 'N':
        break


average = sum(lista[1]) / count
print(f'Total of people {count}')
print(f'Average Age {average}')
print(f'Woman {fcount}')
for c in range(0, len(lista),1):
    if dictonary['age'] > average:
        lista[0].append(dictonary['name'])
print(f'above average: {lista[0]}')
