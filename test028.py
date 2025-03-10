import random
print('Can you guess which number 0,5 i´m thinking?')
nesco=random.randint(0,5)
nmeu=int(input('Type a number '))
if nmeu == nesco:
    print('You´re pretty good')
else:
    print('You´re not that good')