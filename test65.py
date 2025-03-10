conti = str(input('wanna start? [s/n]:')).strip().upper()
if conti == 'S':
    nyuber =[]
    ave = c = 0
    plus = 0
    minus = 9999999999
    while conti != 'N':
        nyuber = int(input('Type a number: '))
        ave += nyuber
        if plus <= nyuber:
            plus = nyuber
        if minus > nyuber:
            minus = nyuber
        conti = str(input('Type if you want to continue [s/n]:')).strip().upper()
        c += 1

    print(f'is the average {ave / c}' )
    print(f'number of terms {c}')
    print(f'Total {plus} and {minus}')
else:
    print('The end!')