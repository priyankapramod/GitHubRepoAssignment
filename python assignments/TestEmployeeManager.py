__author__ = 'priyanka'

from Employee import Employee
from Manager import Manager

"""
Creates two Employee and Manager  objects and calls methods on them for testing purposes.
"""


#test for Employee class


#------calls constructor(__init__)
employee1 = Employee('Kelu', 'Pram', '123123123', 500)

#-----test for giveRaise method
employee1.giveRaise(2.50)
print(employee1.salary)

#------calls constructor(__init__)
employee2 = Employee('Pras', 'Chandra', '333444222', 600)

#-----test for __str__method
print(employee2)
employee2.giveRaise(3.00)
print(employee2.salary)
print(employee2.ssn)



#test for Manager class

#------calls constructor(__init__)
manager1 = Manager( 'VenkataRao', 'Perala', '333666999', 10000,  'Senior Manager', 4000)

#------test for __str__method
print(manager1)

#-----test for giveRaise method.
manager1.giveRaise(4.50)
print(manager1.salary)
manager2 = Manager('Pramod', 'Kumar', '123456789', 25000, 'VicePresident', 10000)
print(manager2.title)
manager3 = Manager('Maa', 'Nagarjuna', '777999222', 9000, 'Director', 2000)
print(manager3.amt_bonus_indollars)
print("\n")



#test on list of employees and managers with giveRaise  method using loop
employee01  =  Employee('Kiran', 'Perala', '123123123', 8000)
employee02  =  Employee('Anusha', 'Datla', '111222333', 7000)
employee03  =  Employee('Krishna', 'Deepthi', '111222333', 7000)
employee04  =  Employee('Fatty', 'Gulzar', '555999222', 6000)

manager01  =  Manager('Ramprasad', 'Duggirala', '276381117', 20000, 'Director', 5000)
manager02  =  Manager('Radha', 'Gopalabatla', '276381126', 22000, 'Deputy Director', 4000)
manager03  =  Manager('Pramod', 'Sivaraju', '275381117', 11000, 'Senior Director', 3000)
manager04  =  Manager('Prasanth', 'Chandras', '096381117', 10000, 'Director', 2000)

# list of employees and managers
employee_manager_list = [employee01, employee02, employee03, employee04, manager01, manager02, manager03, manager04]

for i in range(len(employee_manager_list)):
    employee_manager_list[i].giveRaise(3.15)
    print(employee_manager_list[i].salary)



# test for magic methods
emp1 = Employee('priya', 'pramod', '123123412', 5000)
emp2 = Employee('priya', 'pramod', '231123424', 6000)
emp3 = Employee('kelu', 'pramod', '444777656', 7000)
emp4 = Employee('mano', 'naga', '786678776', 4444 )

print(emp1.firstName)
print(emp2.firstName)
print(emp1 == emp2)
print(emp3 < emp2)
print(emp2 < emp3)
print(emp4 < emp3)


#sort on employee and manager list which uses __lt__ magic method.
employee_manager_list = sorted(employee_manager_list)

for emp in employee_manager_list:
    print(emp)








"" """"
512.5
The employee's first and last name as Pras Chandra and with ssn 333444222 has a salary of 600 $
618.0
333444222
The employee's first and last name as VenkataRao Perala and with ssn 333666999 has a salary of 10000 $
10450.0
VicePresident
2000


8252.0
7220.5
7220.5
6189.0
20630.0
22693.0
11346.5
10315.0
priya
priya
True
True
False
True
The employee's first and last name as Prasanth Chandras and with ssn 096381117 has a salary of 10315 $
The employee's first and last name as Anusha Datla and with ssn 111222333 has a salary of 7220 $
The employee's first and last name as Krishna Deepthi and with ssn 111222333 has a salary of 7220 $
The employee's first and last name as Ramprasad Duggirala and with ssn 276381117 has a salary of 20630 $
The employee's first and last name as Radha Gopalabatla and with ssn 276381126 has a salary of 22693 $
The employee's first and last name as Fatty Gulzar and with ssn 555999222 has a salary of 6189 $
The employee's first and last name as Kiran Perala and with ssn 123123123 has a salary of 8252 $
The employee's first and last name as Pramod Sivaraju and with ssn 275381117 has a salary of 11346 $

"" """
