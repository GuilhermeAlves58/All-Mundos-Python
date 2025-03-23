dict = {'Name': str(input('Type your name ')),
'average': float(input('Type the average '))}
print(f"name is {dict['Name']}")
print(f"average is {dict['average']}")
if dict['average'] < 7.0:
    print('Needs more grade')
elif dict['average'] <  5.0:
    print('failed in the student"s average')
else:
    print('Great average')