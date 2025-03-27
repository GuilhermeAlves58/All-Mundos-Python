golslist = {}
golslist['Name'] = str(input('Name of the player: ')).capitalize()
golslist['Matches'] = int(input(f'How many matches did {golslist['Name']} played: '))
golslist['Total'] = 0
lista = []
for c in range(0,golslist['Matches'],1):
    goalscore = int(input(f'how many goals in the {c} match: '))
    golslist['Total'] += goalscore
    lista.append(goalscore)
    golslist['score'] = lista
print(f"{golslist['Name']} gols: {golslist['score']} total: {golslist['Total']}")