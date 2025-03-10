loanvalue=float(input('what is the loan amount you want to take? D$'))
salaryvalue=float(input('how much is your salary? D$'))
loantime= int(input('How many years will you be paying? D$ '))
installment= loanvalue / (loantime * 12)
minvalue= salaryvalue * 30 / 100
print('To pay {} in {} years the installment will be {}'.format(loanvalue,loantime,minvalue))
if installment <= minvalue:
    print('It is possible  to take a loan')
else:
    print('It is not possible')

