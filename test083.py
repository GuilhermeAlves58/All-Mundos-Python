expresion = (str(input('Type a expression: ').upper().strip()))
openp = expresion.count('(')
closedp = expresion.count(')')
if openp != closedp:
    print('Expression invalid!')
else:
    print('expression valid!')
