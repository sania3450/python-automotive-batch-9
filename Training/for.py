for i in range (1,21):
    if i==13:
        pass
    else:
        print(i)

print("\n")

phone_num = "123-456-7890"

for i in phone_num:
    if i=="-":
        continue
    print(i, end=" ")