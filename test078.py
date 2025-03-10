list = []
c = p = 0
while c < 5:
    num = int(input('Type a number: '))
    list.append(num)
    c += 1
maznum = max(list)
minnum = min(list)
print(f'you have typed {list}')
print(f'The largest number is {maznum} in the position {list.index(maznum) + 1} ')
print(f'The lowest number is {minnum} in the position {list.index(minnum) + 1}')
