import money108

number = float(input('Type a value: '))
print(f'{money108.coin(number)} half:R${money108.half(number)}')
print(f'{money108.coin(number)} double:R${money108.double(number)}')
print(f'{money108.coin(number)} 10 percent increase:R${money108.percent(number)}')
print(f'{money108.coin(number)} 10 percent decrease:R${money108.percentsub(number)}')
