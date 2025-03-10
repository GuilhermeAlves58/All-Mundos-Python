heaviest = 0
lightest = 0
for c in range(1,6,+1):
    weight = float(input('Type your weight: '))
    if c == 1:
        heaviest = weight
        lightest = weight
    else:
        if weight > heaviest:
            heaviest = weight
        if weight < lightest:
            lightest = weight
print(f'{heaviest} kgs')
print(f'{lightest}kgs')
