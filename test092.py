import datetime
info = {'nome': str(input('digite seu nome ')),
    'dianascimento': int(input('digite data de nascimento ')),
    'CLT': int(input('Carteira de trabalho[0 se não tiver]: '))
}
adinfo = {}
if info['CLT'] == 0:
    print(f"nome tem o valor: {info['nome']}")
    print(f"data de nascimento tem o valor: {info['dianascimento']}")
    print(f"Clt tem o valor: {info['CLT']}")
else:
    adinfo = {'Anocontratação': int(input('digite Ano de contratação')), 'salário': int(input('salario: '))}
    aposentadoria = (adinfo['Anocontratação'] + 35) - datetime.date.today().year
    idade =  datetime.date.today().year - info['dianascimento']

    print(f"nome tem o valor: {info['nome']}")
    print(f"data de nascimento tem o valor: {info['dianascimento']}")
    print(f"Clt tem o valor: {info['CLT']}")
    print(f"Ano de contratação tem o valor de :{adinfo['Anocontratação']}")
    print(f"Salário tem o valor de: {adinfo['salário']}")
    print(f"idade tem o valor de: {idade}")
    print(f"aposentadoria tem o valor de: {aposentadoria}")