num = [[],[]]
value = 0
for c in range(1,8):
    value = int(input('Type a value: '))
    if value % 2 == 0:
        num[0].append(value)
    else:
        num[1].append(value)
print(sorted(num[0]))
print(sorted(num[1]))