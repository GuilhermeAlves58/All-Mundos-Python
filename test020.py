import random
part1=str(input('Nome do primeiro grupo '))
part2=str(input('Nome do segundo grupo '))
part3=str(input('Nome do terceiro grupo '))
part4=str(input('Nome do quarto grupo '))
ordem= [part1, part2, part3, part4]
random.shuffle(ordem)
print(ordem)
