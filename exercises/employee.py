"""
Write a script that inputs the hourly wage of 
an employee and the number of hours worked and 
calculates and displays the employee s salary.

"""

hourly_wage=float(input('Enter your hourly wage: '))
hours=int(input('How many hours have you worked? '))
salary=hourly_wage * hours
print('Your salary is: ' + str(salary) + ' $')


"""
The employee will receive
100$ if he/she has worked more than 40 hours
"""

salary=hourly_wage * hours
if hours > 40:
    salary +=100
    print("Your salary is:" + str(salary) + "$")
