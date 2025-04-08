def readint(integer = '' ):
    integer = str(input('Type a number: '))
    value = 0

    while True:
        if integer.isnumeric():
            value = int(integer)
            return value
        else:
            integer = str(input('Error Type number: '))


n = readint()
print(f'You typed the number:{n}')
