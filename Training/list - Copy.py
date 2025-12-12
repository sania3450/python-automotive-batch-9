def find_smallest_num(num):
    if not num:
        return None  
    return min(num)

my_list = [10, 4, 30, 20, 5, 92]
smallest = find_smallest_num(my_list)
print(f"The Smallest number is: {smallest}")

