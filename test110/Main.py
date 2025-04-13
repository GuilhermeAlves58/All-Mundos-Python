import money110
v = float(input('Digite o preço: R$'))
print(f'A metade de {money110.forma(v)} é {money110.metade(v, True)}')
print(f'O dobro de {money110.forma(v)} é {money110.dobro(v, True)}')
print(f'Aumentando 10%, temos {money110.aumentar(v, 10, True)}')
print(f'Diminuindo 13%, temos {money110.reduzir(v, 13, True)}')