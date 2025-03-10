product = ''
total = above1000 = pr = 0
while True:
    name = str(input('Type the name of your product: ')).strip().capitalize()
    prize = int(input('Type the cost: '))
    total += prize
    if prize > pr:
        pr = prize
        product = name
    if prize >= 1000:
        above1000 += 1
    cys = str(input('Wanna continue: [Y/N] ')).upper().strip()
    if cys == 'N':
        break
print(f'Total: {total} and {above1000}and the more expensive {product}')