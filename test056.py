man = 0
women = 0
average = 0
manage= 0
manname= ''
for c in range(1,5,+1):
    print(f'{c} Person')
    name = str(input('Type your name: '))
    age = int(input('Type your age: '))
    sex = str(input('M/F: ')).upper()
    average += age /4
    if sex == 'F' and age < 20:
        women += 1
    if sex == 'M' and age > manage:
        manage = age
        manname = name
print(f'The average age is {average} and the oldest man is {manname}  and there are {women} women under 20 years')

