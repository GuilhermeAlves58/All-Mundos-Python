from django.utils.http import escape_leading_slashes

num=int(input('Type a number '))
print('''Which coversion base do you want
[1] convert to binary
[2] convert to oct
[3] convert to hexa''')
option = int(input('Your option: '))
binary = bin(num)
octal= oct(num)
hexadec= hex(num)
if option == 1:
    print(binary[2:])
elif option == 2:
    print(octal[2:])
elif option == 3:
    print(hexadec[2:])
else:
    print('This is not a valid value')
