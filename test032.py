from datetime import date
ano=int(input('Type the year you want to analyze, if you want to see the current year type 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano% 400 == 0:
    print('É bissexto {}'.format(ano))
else:
    print('Não é bissexto')

