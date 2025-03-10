numer = []
total = 0
c = 0
while numer != 999:
    numer= int(input('Type a number[999 to stop]:  '))
    if numer != 999:
        total += numer
        c += 1
    else:
        print(f'{c}')
print(total)