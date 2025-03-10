allnumber = ('Zero','one','two','three','four','six','seven','eight','nine','ten','eleven','twelve','thirteen',
'fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty')
yourcoiche = int(input('Type a number from 0 to 20: '))
while yourcoiche > 20:
    yourcoiche = int(input('Type a number from 0 to 20: '))
if yourcoiche == 0:
    print(f'you typed number {allnumber[0]}')
else:
    print(f'You typed  number {allnumber[yourcoiche - 1]}')



