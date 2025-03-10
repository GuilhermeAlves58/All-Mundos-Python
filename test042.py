Aside = int(input('Type the first triangle side: '))
Bside = int(input('Type the second triangle side: '))
Cside = int(input('Type the third triangle side: '))

if Aside < Bside + Cside and Bside < Aside + Cside and Cside < Aside + Bside:
    print('it is possible to make a triangle')
    if Aside == Bside == Cside:
        print('EQUILÁTERO')
    elif Aside == Bside != Cside or Bside == Cside != Aside or Cside == Aside != Bside:
        print('ISÓSCELES')
    elif Aside != Bside != Cside != Aside:
        print('ESCALENO')
else: print('it is impossible')


