class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def calculate_net_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()


try:
    # Input from user
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))

    if basic_salary <= 0:
        raise ValueError("Basic salary cannot be negative")

    # Create object
    emp = Employee(emp_id, name, basic_salary)

    # Output
    print("\nEmployee Details")
    print("Employee ID:", emp.emp_id)
    print("Name:", emp.name)
    print("Basic Salary:", emp.basic_salary)
    print("HRA:", emp.calculate_hra())
    print("DA:", emp.calculate_da())
    print("Net Salary:", emp.calculate_net_salary())

except ValueError as e:
    print("Invalid input  :", e)

else:
    print("\nSalary calculated successfully ")

#finally:
#    print("Program finished.")
