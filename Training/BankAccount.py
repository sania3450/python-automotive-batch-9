class BankAccount:
    def __init__(self, name, age, principal, time):
        self.name = name
        self.age = age
        self.principal = principal
        self.time = time
        self.rate = 8   # interest rate for senior citizens

    def calculate_interest(self):
        # check if the person is a senior citizen
        if self.age < 60:
            raise ValueError("Interest is available only for senior citizens.")

        interest_amount = self.principal + (self.principal * self.rate * self.time) / 100
        return interest_amount


try:
    print("---- Bank Account Details ----")

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    principal = float(input("Enter principal amount: "))
    time = float(input("Enter time in years: "))

    account = BankAccount(name, age, principal, time)
    result = account.calculate_interest()

    print("\n---- Interest Details ----")
    print("Name:", account.name)
    print("Age:", account.age)
    print("Total Amount after Interest:", result)

except ValueError as error:
    print("\nInput Error:", error)

except Exception:
    print("\nSomething went wrong. Please try again.")

else:
    print("\nInterest calculated successfully.")

finally:
    print("Thank you for using the bank system.")
