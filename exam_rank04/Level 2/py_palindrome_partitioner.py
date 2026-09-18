"""Given a string `s`, find the minimum number of cuts needed to partition it such that every resulting substring is a palindrome.

A cut divides the string between two characters. With `c` cuts, the string is split into `c + 1` substrings. We want the minimum number of cuts `c` such that all parts are palindromes.

Return this minimum number of cuts (an integer).

Constraints:
- An empty string or a string of length 1 is already a palindrome -> 0 cuts.
- If the entire string is already a palindrome -> 0 cuts.
- In the worst case (all characters are distinct), the result is len(s) - 1 cuts.
FUNCTION SIGNATURE
def palindrome_partitioner(s: str) -> int:
EXAMPLES
palindrome_partitioner("aab")->1
palindrome_partitioner("aba")->0
palindrome_partitioner("abc")->2"""

def is_palindrome(text):
    return text == text[::-1]
def find_min_cuts(s, dp, end):
    biggest = end
    for start in range(end + 1):
        part = s[start:end + 1]
        if is_palindrome(part):
            if start == 0:
                biggest = 0
            else:
                cuts = dp[start - 1] + 1
                biggest = min(biggest, cuts)
    return biggest
def palindrome_partitioner(s):
    if len(s) <= 0:
        return 0
    dp = [0] * len(s)
    for end in range(len(s)):
        dp[end] = find_min_cuts(s, dp, end)
    return dp[-1]

print(palindrome_partitioner("aac"))
print(palindrome_partitioner("aba"))
print(palindrome_partitioner("abc"))