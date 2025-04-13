import money
v = float(input('Digite o preço: R$'))
print(f'A metade de {money.forma(v)} é {money.metade(v, True)}')
print(f'O dobro de {money.forma(v)} é {money.dobro(v, True)}')
print(f'Aumentando 10%, temos {money.aumentar(v, 10, True)}')
print(f'Diminuindo 13%, temos {money.reduzir(v, 13, True)}')