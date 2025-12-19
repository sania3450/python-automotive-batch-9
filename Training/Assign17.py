students = []

# taking input for 20 students
for i in range(20):
    print(f"\nEnter details for student {i + 1}")
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    students.append((name, surname))

# dictionary to keep only one student per name
unique_students = {}

for name, surname in students:
    if name not in unique_students:
        unique_students[name] = surname

# display result
print("\nStudents after removing duplicate names:\n")
for name, surname in unique_students.items():
    print(name, surname)
