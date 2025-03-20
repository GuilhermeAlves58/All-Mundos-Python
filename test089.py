marks = [[],[],[]]
c = ave = end = 0
clone = []
result = []
while True:
    marks[0].append(str(input('Name: ')))
    marks[1].append(int(input('grade1: ')))
    marks[2].append(int(input('grade2: ')))
    stop = str(input('Type[Y/N] to stop: ')).upper().strip()
    ave = (marks[1][c] + marks[2][c])/ 2
    clone.append(marks[0])
    result.append(ave)
    print(f"{marks[0][c]}'s marks is {ave}")
    c += 1
    if stop == 'N' :
        break
    elif stop != 'Y':
        stop = str(input('Type[Y/N] to stop: ')).upper().strip()


while True:
    end = int(input(f"Type the number to show the students's marks {len(marks[0]) - 1} total "))
    if end == 999:
        break
    else:
        print(f"{clone[end][end]}'s marks is {result[end]}")