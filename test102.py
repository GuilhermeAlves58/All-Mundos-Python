def fact(num,show=False):
    global many
    c = 1
    while many != 1:
        c =  c * many
        if show == True:
            print(f'{c} x {many - 1}')
        many -= 1
    print(c)


many = int(input('Type how many: '))
fact(many,show=True)