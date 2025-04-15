def readmoney(msg):
    valid = False
    while not valid:
        inputt = str(input(msg)).replace(',','.').strip()
        if inputt.isalpha() or inputt == '':
            print(f'{inputt} invalid')
        else:
            valid = True
            return float(inputt)
