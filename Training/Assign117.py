# pre defined list of 20 students 
students = [
    ("Aditi", "Sharma"),
    ("Amit", "Patel"),
    ("Priyal", "Singh"),
    ("Aditi", "Mehta"),
    ("Neha", "Gupta"),
    ("Anisha", "Patel"),
    ("Suresh", "Kumar"),
    ("Anita", "Roy"),
    ("Vikas", "Malhotra"),
    ("Pooja", "Jain"),
    ("Nehal", "Jurel"),
    ("Ravi", "Kapoor"),
    ("Sunita", "Iyer"),
    ("Aakash", "Bansal"),
    ("Rohit", "Agarwal"),
    ("Priya", "Verma"),
    ("Kiran", "Reddy"),
    ("Manoj", "Yadav"),
    ("Ankita", "Singh"),
    ("Dipa", "Joshi")
]

# dict to keep track of names and all their surnames
name_surnames = {}

for name, surname in students:
    if name not in name_surnames:
        name_surnames[name] = {surname}  # set is used to store unique surnames for each name.
    else:
        name_surnames[name].add(surname)

final_students = [] #creates an empty list to store the final student records.

for name, surnames in name_surnames.items():
    
    for n, s in students:
        if n == name: #checks if the name in the original list matches the current name from the dictionary.
            final_students.append((n, s))
            break

# Display result
print("\nStudents after keeping only one record per duplicate name:\n")
for name, surname in final_students:
    print(name, surname)
