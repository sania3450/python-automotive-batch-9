with open("example1.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")
    print("Content written to example1.txt")

with open("example1.txt", "r") as file:
    data = file.read()
    print(data)