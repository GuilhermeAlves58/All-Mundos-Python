pn = int(input('Type the first number: '))
r =  int(input('Type the Ratio: '))
lastterm = pn + (10-1) * r
for c in range(pn, lastterm, +r):
    print(c, end='-> ')
print('IT´s over Anakin')