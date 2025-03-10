people = []
heaviest = lightest = 0

while True:
    name = input('Type your name: ')
    weight = float(input('Type your weight: '))
    person = [name, weight]
    people.append(person)

    if len(people) == 1:  # Primeiro cadastro
        heaviest = lightest = weight
    else:
        if weight > heaviest:
            heaviest = weight
        if weight < lightest:
            lightest = weight

    wantcount = input('Type if you want to continue:[Y/N] ').strip().upper()
    if wantcount == 'N':
        break
    elif wantcount != 'Y':
        print('Invalid! Type again.')

num_people = len(people)

print(f'Number of people: {num_people}')

print('The heaviest people:')
for p in people:
    if p[1] == heaviest:
        print(f' - {p[0]} with {p[1]} kg')

print('The lightest people:')
for p in people:
    if p[1] == lightest:
        print(f' - {p[0]} with {p[1]} kg')
