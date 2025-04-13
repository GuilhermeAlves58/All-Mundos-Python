def half(n = 0):
    return n / 2

def double(n = 0):
    return n * 2

def percent(n = 0):
    return  n + (n * 10/100)

def percentsub(n = 0):
    return n - (n *10/100)

def coin(prize = 0,coin ='R$'):
    return f'{coin}{prize}'.replace('.', ',')