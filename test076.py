tupla = ('lápis', 1.75,
        'Borracha', 2.00,
        'Caderno', 15.90,
        'Estojo', 25.00,
        'transferidor', 4.20,
        'compasso', 9.99,
        'mochila', 120.32,
        'Canetas', 22.30,
        'livros', 34.90)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]}',end= ' ')
    else:
        print(f'{tupla[pos]}')