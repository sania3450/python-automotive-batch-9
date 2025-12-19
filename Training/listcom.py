num = [1,2,3,4,5]

cube = [x**3 for x in num]
print(cube)

#Condition statement with list

stud = [96, 78, 45, 50, 74, 81]

result_pass =[i if i>=50 else "Fail" for i in stud]
print(result_pass)

topper = [i for i in stud if i>=80]
print(topper)