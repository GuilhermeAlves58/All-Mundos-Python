userheight= float(input('Type your height: Ms '))
userweight= int(input('Type your weight: KGs '))
imc = userweight / userheight ** 2
print('Your IMC is {:.2f}'.format(imc))
if imc < 18.5:
    print('Underweight')
elif imc < 25.0:
    print('Ideal weight')
elif imc < 30.0:
    print('obesity')
elif imc < 40.0:
    print('Morbid obesity')

