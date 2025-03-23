from random import randint
from operator import itemgetter
dictplayer = {'Player1': randint(0,6),
'Player2': randint(0,6),
'Player3': randint(0,6),
'Player4': randint(0,6)
}
print(f"Player1: {dictplayer['Player1']}")
print(f"Player2: {dictplayer['Player2']}")
print(f"Player3: {dictplayer['Player3']}")
print(f"Player4: {dictplayer['Player4']}")
ranking = []
ranking = sorted(dictplayer.items(), key = itemgetter(1), reverse = True)
for i,v in enumerate(ranking):
    print(f'{i + 1} place: {v[0]} with {v[1]}')