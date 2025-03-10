tenx = 0
while True:
    mathta = int(input('Type another math table: '))
    if mathta <= 0:
        break
    while tenx <= 10:
        print(f'{mathta} X {tenx} = {mathta * tenx}')
        tenx +=1
    if tenx > 10:
        tenx = 0

