# Employee payroll system using single inheritance

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Basic Salary: ₹", self.basic_salary)

class Payroll(Employee):
    def calculate_salary(self):
        self.hra = 0.20 * self.basic_salary
        self.da = 0.10 * self.basic_salary
        self.pf = 0.12 * self.basic_salary
        self.gross = self.basic_salary + self.hra + self.da
        self.net = self.gross - self.pf

    def display_payroll(self):
        self.display_employee()
        print("HRA (20%): ₹", self.hra)
        print("DA (10%): ₹", self.da)
        print("PF (12%): ₹", self.pf)
        print("Gross Salary: ₹", self.gross)
        print("Net Salary: ₹", self.net)

emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
basic = float(input("Enter Basic Salary: "))
emp = Payroll(emp_id, name, basic)
emp.calculate_salary()
print("\n===== Employee Payroll =====")
emp.display_payroll()
