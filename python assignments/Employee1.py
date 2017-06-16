__author__ = 'priyanka.'

from functools import total_ordering

@total_ordering


class Employee:
    """ One object of class Employee represents one  employee's first name,
        last name, social security number and his salary
"""
#this is the basic constructor. Here  the current Employee's firstname, lastname, social security number and salary values get assigned
#as per the parameters
    def __init__(self, first_name, last_name, ssn, salary):
        self.firstName = first_name
        self.lastName = last_name
        self.ssn = ssn
        self.salary = salary


#the __str__( ) method is used to convert a Employee object
# into a string
    def __str__(self):
        return "The employee's first and last name as %s %s and with ssn %s has a salary of %d $ " % (self.firstName, self.lastName, self.ssn, self.salary)



#This method gives hike to salary of current Employee's object.
    def giveRaise(self, percentRaise):
        self.salary  =  self.salary + (self.salary * (percentRaise / 100))









emp1 = Employee('priya', 'pramod', '123123412', 5000)
emp2 = Employee('priya', 'pramod', '231123424', 6000)
emp3 = Employee('kelu', 'pramod', '444777656', 7000)
emp4 = Employee('mano', 'naga', '786678776', 4444 )

print(emp1.firstName)
print(emp2.firstName)
print(emp1 == emp2)#
print(emp3 < emp2)#
print(emp2 < emp3)#
print(emp4 < emp3)#
