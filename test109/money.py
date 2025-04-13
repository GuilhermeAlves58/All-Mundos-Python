def forma(msg):
    a = f'R${msg:.2f}'.replace('.',',')
    return a

def metade(n, show=False):
    m = n / 2
    if show:
        return forma(m)
    return m

def dobro(n, show=False):
    d = n * 2
    if show:
        return forma(d)
    return d

def aumentar(n, p, show=False):
    a = n + (n * (p / 100))
    if show:
        return forma(a)
    return a

def reduzir(n, p, show=False):
    a = n - (n * (p / 100))
    if show:
        return forma(a)
    return a

def resumo(prize = 0,taxa = 10, taxade = 5):
    print(f'valor:{forma(prize)}')
    print(f'Dobro:{dobro(prize,True)}')
    print(f'Metade:{metade(prize,True)}')
    print(f'Aumento:{aumentar(prize,taxa,True)}')
    print(f'Redução:{reduzir(prize,taxa,True)}')