def cont(begin,stop,num):
    for c in range(1,11,1):
        print(c, end= ' ')
    print('')
    for v in range(10,0,-2):
        print(v,end= ' ')
    print('')
    if ini < final:
        for b in range(ini,final + 1,num):
            print(b, end= ' ')
    else:
        for x in range(ini, final, -num):
            print(x, end=' ')


ini = int(input('Inicio: '))
final = int(input('final: '))
num = int(input('casas: '))

cont(ini,final,num)