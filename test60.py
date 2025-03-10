'''from math import factorial
fnumber = int(input('Type a number: '))
f = factorial(fnumber)
print(f'{f} is the factorial')'''
fnumber = int(input('Type a number: '))
f =  fnumber
c = 1
while f > 0:
    print(f'{fnumber}! {f} x {f-1}',end= ' ')
    c *= f
    f -= 1
print(f'={c}')