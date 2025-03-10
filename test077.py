tup =  ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'grátis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in tup:
    print(f'\n{p} and the vogals are',end=' ')
    for letter in p:
        if letter.lower() in 'aeiou':
            print(f'{letter}',end='')