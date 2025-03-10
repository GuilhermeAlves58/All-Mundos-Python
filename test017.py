import math
catetovertical=float(input('Digite o valor do cateto '))
catetohorizontal= float(input('Digite o valor do segundo cateto '))
hipotenusa= math.sqrt((catetovertical**2) + (catetohorizontal**2))
print('A hipotenusa é {:.2f}'.format(hipotenusa))