R1= float(input('Typer the value of the triangle edge '))
R2=float(input('Type the value of the second triangle edge '))
R3=float(input('Type the value of the third triangle  edge '))
if R1 < R2 + R3 and R2 < R1 + R3 and R3 < R2 + R1:
    print('It is possible to make a triangle')
else:
    print('It is not possible to make a triangle')

