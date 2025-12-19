for i in range(2):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Sum:", num1 + num2 )


for _ in range(3):  # allow 3 operations
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Choose operation: "))
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result:", a + b)
    elif choice == 2:
        print("Result:", a - b)
    elif choice == 3:
        print("Result:", a * b)
    elif choice == 4:
        print("Result:", a / b)
