



from Employee1 import Employee

class Manager  (Employee):
#this is the basic constructor. As this class is a sub-class of Employee, first calls Employee's constructor
#and initializes that part of the object
# and all other values are assigned as per parameters passed.
    def __init__(self, first_name, last_name, ssn, salary, title, amt_bonus_indollars):
        Employee.__init__(self, first_name, last_name, ssn, salary)
        self.title = title
        self.amt_bonus_indollars = amt_bonus_indollars


#




