lis = []
for c in range(0,5):
    n = int(input('Type a number: '))
    if c == 0 or n > lis[-1]:
        lis.append(n)
    else:
        pos = 0
        while pos < len(lis):
            if n <= lis[pos]:
                lis.insert(pos,n)
                break
                pos += 1
print(f'{lis}')
'''c sempre será  o primeiro número e n sempre será maior do que o último valor:
adiciona o valor na lista.
enquanto posição for menor do que o tamanho da lista.
 se n for menor ou igual lista na pos.
inserir na posição o numero e quebrar o loop'''

#litata = []
#c = 0
#while c < 5:
#    litata.append(int(input('Type a number ')))
#    c += 1
#print(sorted(litata))
