def readint(num=0):
    while True:
        try:
            intteger = int(input('Type a integer: '))
        except (ValueError, TypeError):
            print('Error:Type a interger')
            continue
        except (KeyboardInterrupt):
            print('interrupted by the user')
            return 0
        else:
            return intteger


def readfloat(num=0):
    while True:
        try:
            floatnum = float(input('Type a Float: '))
        except(ValueError, TypeError):
            print('Error:Type a float')
        except(KeyboardInterrupt):
            print('interrupted by the user')
            return 0
        else:
            return floatnum


print(f'interger: {readint()} and float: {readfloat()}')
