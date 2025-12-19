ev_count = 0
od_count = 0

for i in range(1,11):
    num = int(input(f"Enter number {i}: "))

    if num % 2 == 0:
        ev_count += 1
    else:
        od_count += 1

print(f"Total Even numbers are = {ev_count}")
print(f"Total Odd numbers are = {od_count}")

