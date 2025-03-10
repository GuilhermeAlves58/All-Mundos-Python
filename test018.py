import math
Angulo= float(input('Digite os graus '))
conradi= math.radians(Angulo)
Sen= math.sin(conradi)
Con= math.cos(conradi)
Tan= math.tan(conradi)
print('O sen é {:.2f}, con {:.2f} e a Tan {:.2f}'.format(Sen, Con, Tan))