terms = int(input('Type how many terms do you  want to show: '))
a = 0
b = 1
c = a + b
x = 0
while x < terms:
    c = a + b
    print(c)
    a = b
    b = c
    x += 1
