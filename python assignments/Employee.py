__author__ = 'priyanka.'


"""
File employeeDoc
Defines class Employee and tests it by creating  Employee objects and calling methods on them.
"""

class Employee:
    """
    One object of class Employee represents one  employee's first name,
    last name, social security number and his salary
    """
    def __init__(self, first_name, last_name, ssn, salary):
        """
        sets firstName, lastName, ssn and salary of the object to respective values passed by the client as parameters.
        """
        self.firstName = first_name
        self.lastName = last_name
        self.ssn = ssn
        self.salary = salary



    def __str__(self):
        """
        Returns a sentence that tells the first name, last name, ssn and salary  of the employee object.
        """
        return "The employee's first and last name as %s %s and with ssn %s has a salary of %d $ " % (self.firstName, self.lastName, self.ssn, self.salary)




    def giveRaise(self, percentRaise):
        """
        This method gives hike to salary of current Employee's object.
        """
        self.salary  =  self.salary + (self.salary * (percentRaise / 100))




    def __eq__(self, other):
        """
        This magic method tests whether both first and last name of employee are equal or not
        """
        return self.firstName==other.firstName and self.lastName==other.lastName


    def __lt__(self, other):
        """
       this method checks the caller's object name is less than the compared object's name.
       first comes the last name and then the firstname of employee in comparison
       here testing is done lexicographically.
       """
        if self.lastName<other.lastName:
            return True
        elif self.lastName > other.lastName:
            return False
        else:  # lastNames are equal
            return self.firstName < other.firstName




if __name__ == "__main__":
    print ("Employee.__doc__=" + str(Employee.__doc__))
    print ("Employee.__init__.__doc__=" + str(Employee.__init__.__doc__))
    print ("Employee.giveRaise.__doc__=" + str(Employee.giveRaise.__doc__))
    print ("Employee.__str__.__doc__=" + str(Employee.__str__.__doc__))
    print ("Employee.__eq__.__doc__=" + str(Employee.__eq__.__doc__))
    print ("Employee.__lt__.__doc__=" + str(Employee.__lt__.__doc__))


"""
Employee.__doc__=
    One object of class Employee represents one  employee's first name,
    last name, social security number and his salary

Employee.__init__.__doc__=
        sets firstName, lastName, ssn and salary of the object to respective values passed by the client as parameters.

Employee.giveRaise.__doc__=
        This method gives hike to salary of current Employee's object.

Employee.__str__.__doc__=
        Returns a sentence that tells the first name, last name, ssn and salary  of the employee object.

Employee.__eq__.__doc__=
        This magic method tests whether both first and last name of employee are equal or not

Employee.__lt__.__doc__=
       this method checks the caller's object name is less than the compared object's name.
       first comes the last name and then the firstname of employee in comparison
       here testing is done lexicographically.
"""
