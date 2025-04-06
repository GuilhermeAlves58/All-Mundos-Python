def fact(num):
    global many
    c = 1
    while many != 1:
        c =  c * many
        many -= 1
    print(c)


many = int(input('Type how many: '))
fact(many)