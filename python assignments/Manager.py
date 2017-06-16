__author__ = 'priyanka'

from Employee import Employee

"""
File managerDoc
Defines class Manager and tests it by creating  manager objects and calling methods on them.
"""


class Manager  (Employee):
    """
    One object of class Manager represents one
    manager's title and his bonus amount in dollars.
    """

    def __init__(self, first_name, last_name, ssn, salary, title, amt_bonus_indollars):
        """
        sets firstName, lastName, ssn and salary, title and bonus amount of the object to respective values passed by the client as parameters.
        """
        Employee.__init__(self, first_name, last_name, ssn, salary)
        self.title = title
        self.amt_bonus_indollars = amt_bonus_indollars




if __name__ == "__main__":
    print ("Manager.__doc__=" + str(Manager.__doc__))
    print ("Manager.__init__.__doc__=" + str(Manager.__init__.__doc__))



"""
Manager.__doc__=
    One object of class Manager represents one
    manager's title and his bonus amount in dollars.

Manager.__init__.__doc__=
        sets firstName, lastName, ssn and salary, title and bonus amount of the object to respective values passed by the client as parameters.
"""












