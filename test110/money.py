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