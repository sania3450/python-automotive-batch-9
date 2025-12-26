def countDistinctPalindromicSubsequences(s):
    n = len(s)
    palindromes = set()

    # Generate all subsequences using bitmask
    for mask in range(1, 1 << n):
        subseq = ""
        for i in range(n):
            if mask & (1 << i):
                subseq += s[i]

        # Check if subsequence is palindrome
        if subseq == subseq[::-1]:
            palindromes.add(subseq)

    return len(palindromes)
s = "nayan"
print(countDistinctPalindromicSubsequences(s))
