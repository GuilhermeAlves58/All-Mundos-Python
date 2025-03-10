numer = []
n1 = n2 = 0
while True:
    numer = int(input('Type a value:[999 to break] '))
    if numer == 999:
        break
    n2 += 1
    n1 += numer
print(f'the total {n1} and {n2} terms')