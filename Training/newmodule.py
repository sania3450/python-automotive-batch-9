#program using sys module that accepts numbers as command-line arguments
import sys

nums = list(map(int, sys.argv[1:]))

total = sum(nums)
average = total / len(nums)

print("Sum =", total)
print("Average =", average)
