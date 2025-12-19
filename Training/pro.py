# Function to check if student has a good grade or not
def progress(marks, total_marks=100):

    percentage = (marks / total_marks) * 100
    
    if percentage >= 60:
        return "Pass"
    else:
        return "Fail"

stud_marks = float(input("Enter student's marks: "))
result = progress(stud_marks)
print("Student score:", stud_marks)
print("Result:", result)

