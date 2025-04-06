import datetime
def votes(year):
    global biryear
    data = datetime.date.today().year
    biryear = data - biryear
    if biryear > 65:
        print(f'{biryear} is optional')
    elif biryear >= 18:
        print(f'{biryear} is Mandatory')
    elif biryear > 15 :
        print(f'{biryear} is optional')
    else:
        print(f'{biryear} is not allowed')

biryear = int(input('Typer your birthyear: '))
votes(biryear)