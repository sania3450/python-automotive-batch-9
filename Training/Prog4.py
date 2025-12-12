num1 = int(input("Enter 1st number: = "))
num2 = int(input("Enter 2nd Number: = "))
num3 = int(input("Enter 3rd Number: = "))

if (num1 >= num2) and (num1 >= num3):
    print("The num1 is Largest ")
elif (num2 >= num1) and (num2 >= num3):
    print("The num2 is Largest ")
else:
    print("The num3 is Largest")