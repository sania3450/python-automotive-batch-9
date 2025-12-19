# function to check if student has a good grade or not
def progress(marks, total_marks=100):

    percentage = (marks / total_marks) * 100
    
    if percentage >= 60:
        return "Pass"
    else:
        return "Fail"

stud_marks = 82
print("Student score:", stud_marks)
print("Result:", progress(stud_marks)) 

stud_marks = 59
print("Student score:", stud_marks)
print("Result:", progress(stud_marks))  