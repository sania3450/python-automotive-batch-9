# Parent class (Encapsulation)
class Student:
    def __init__(self, student_id):
        self.__student_id = student_id   # private variable

    # getter method (to access private data)
    def get_student_id(self):
        return self.__student_id


# Child class (Inheritance)
class OlympiadStudent(Student):
    def check_queue(self):
        # get student id from parent class
        sid = self.get_student_id()

        # extract number part from STD_004 → 4
        number = int(sid.split("_")[1])

        # check even or odd
        if number % 2 == 0:
            print(sid, "belongs to Queue 1 (Even ID – allowed first)")
        else:
            print(sid, "belongs to Queue 2 (Odd ID – allowed later)")


# ---------------- MAIN PROGRAM ----------------

print("Olympiad Student Queue System")

# take input for 10 students
for i in range(10):
    student_id = input("Enter Student ID (STD_001 to STD_010): ")

    s = OlympiadStudent(student_id)
    s.check_queue()

    print("------------------------")
