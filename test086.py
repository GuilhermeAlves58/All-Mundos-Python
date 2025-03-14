lista = [[], [], []]
new_line = 0
while True:
    value = int(input('Type a value: '))
    new_line += 1
    if new_line <= 3:
        lista[0].append(value)
    elif new_line <= 6:
        lista[1].append(value)
    elif new_line <= 9:
        lista[2].append(value)
    if new_line == 9:
        break
print(lista[0])
print(lista[1])
print(lista[2])