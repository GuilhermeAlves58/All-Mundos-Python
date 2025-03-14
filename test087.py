lista = [[], [], []]
new_line = 0
pares = 0
while True:
    value = int(input('Type a value: '))
    new_line += 1
    if new_line <= 3:
        lista[0].append(value)
    elif new_line <= 6:
        lista[1].append(value)
    elif new_line <= 9:
        lista[2].append(value)
    if value % 2 == 0:
        pares += value
    if new_line == 9:
        break
print(lista[0])
print(lista[1])
print(lista[2])
soma_terceira_coluna = lista[0][2] + lista[1][2] + lista[2][2]
maior_valor_segunda_linha = max(lista[1])
print(f'A) Soma de todos os valores pares digitados: {pares}')
print(f'B) Soma dos valores da terceira coluna: {soma_terceira_coluna}')
print(f'C) O maior valor da segunda linha: {maior_valor_segunda_linha}')
