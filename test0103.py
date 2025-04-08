def ficha(names = '<unknown>',gols = 0):
    print(f'{names}´s gols : {gols}')

name = str(input('name of the player: ')).strip().capitalize()
gol = int(input('Gols: '))
player = len(name)
if player == 0:
    ficha('<unknown>',gol)
else:
    ficha(name,gol)


