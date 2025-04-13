import money

number = float(input('Type a value: '))
print(f'{money.coin(number)} half:R${money.half(number)}')
print(f'{money.coin(number)} double:R${money.double(number)}')
print(f'{money.coin(number)} 10 percent increase:R${money.percent(number)}')
print(f'{money.coin(number)} 10 percent decrease:R${money.percentsub(number)}')
