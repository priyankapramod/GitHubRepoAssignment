

from Employee1 import Employee
from Manager1 import Manager



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

employee_manager_list = sorted(employee_manager_list)

for emp in employee_manager_list:
    print(emp)



