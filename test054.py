import datetime
day = datetime.date.today().year
contadorse = 0
contadorminor = 0
for c in range(1, 7, +1):
    bithrday = int(input(f'Type the birthday of the {c} person: '))
    if day - bithrday  >= 18:
        contadorse += 1
    else:
        contadorminor += 1
print(f'{contadorse} are senior')
print(f'{contadorminor} are minor')
