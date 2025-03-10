salary= float(input('Type your salary '))
newsalary= (salary*0.15)+ salary
if salary <= 1250.00:
    print('Your new salary is {}'.format(newsalary))
else:
    print('your new salary is  {}'.format(salary*0.10 + salary))