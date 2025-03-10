number= int(input('Type a number '))
cutnumber= str(number)
u= number// 1% 10
t= number// 10% 10
hundred= number// 100% 10
thousand= number// 1000% 10
print('The number has {} units'.format(u))
print('The number has {} tens'.format(t))
print('The number has {} hundred'.format(hundred))
print('The number has {} thousand'.format(thousand))