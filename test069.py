above18 = less20w = mantotal = 0
while True:
    age = int(input('Type a age: '))
    gender = str(input('Type if male or female[f/M]:')).upper().strip()
    while gender not in 'MF':
        gender = str(input('Type if male or female[f/M]:')).upper().strip()
    yn = str(input('wanna continue: [Y/N]')).upper().strip()
    while yn not in 'YN':
        yn = str(input('wanna continue: [Y/N]')).upper().strip()
    if age > 18:
        above18 += 1
    if gender == 'M':
        mantotal += 1
    elif gender == 'F' and age < 20:
        less20w += 1
    if  yn == 'N':
        break
print(f'{above18} {less20w} {mantotal}')