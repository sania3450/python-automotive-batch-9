n_th= int(input("How many terms? \n"))

n1, n2 = 0, 1
count = 0

if n_th <= 0:
   print("Please enter a positive integer")
elif n_th == 1:
   print("Fibonacci sequence upto",n_th,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n_th:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1