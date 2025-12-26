class Employee:
    def __init__(self, emp_id, name, basic_salary, hra_percent, da_percent):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        self.hra_percent = hra_percent
        self.da_percent = da_percent

    def calculate_hra(self):
        return self.basic_salary * (self.hra_percent / 100)

    def calculate_da(self):
        return self.basic_salary * (self.da_percent / 100)

    def calculate_net_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()


try:
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))
    hra_percent = float(input("Enter HRA percentage: "))
    da_percent = float(input("Enter DA percentage: "))

    if basic_salary <= 0:
        raise ValueError("Basic salary must be greater than zero")
    if hra_percent < 0 or da_percent < 0:
        raise ValueError("Percentages cannot be negative")

    emp = Employee(emp_id, name, basic_salary, hra_percent, da_percent)

    print("\n===========Employee Details============")
    print("Employee ID:", emp.emp_id)
    print("Name:", emp.name)
    print("Basic Salary:", emp.basic_salary)
    print("HRA Amount:", emp.calculate_hra())
    print("DA Amount:", emp.calculate_da())
    print("Net Salary:", emp.calculate_net_salary())

except ValueError as e:
    print("Invalid input  :", e)

else:
    print("\nSalary calculated successfully ")