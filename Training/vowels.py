def count_vowel(v):

    vowels = "aeiouAEIOU"

    return sum(1 for char in v if char in vowels)

strg = "A Dog is Cute"
count = count_vowel(strg)
print(f"The number of vowels in the sentence is: {count}")