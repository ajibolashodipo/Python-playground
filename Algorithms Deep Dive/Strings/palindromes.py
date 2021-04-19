# 3 methods

# 2 pointers from the center
# 2 pointers from the ends
# compare with reverse

# almost palindrome: does the string become a palindrome if we remove one character?

def valid_subPalindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def almost_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # returns true if any of the two broken off substrings go on to become full palindromes. else, returns false
            return valid_subPalindrome(s, left + 1, right) or valid_subPalindrome(s, left, right - 1)
        left += 1
        right -= 1
    return True


# WRONG SOLUTION. DOESN'T COVER ALL POSSIBLE CASES. FIRST ATTEMPT.
def palindrome(s):
    if len(s) <= 2:
        return True

    left = 0
    fixed = len(s) - 1
    right = len(s) - 1
    count = 0

    while left < right:

        if s[left] != s[right]:
            count += 1

            if count > 1:
                return False

            # left index stays
            arr = list(s)
            del arr[right]
            s = "".join(arr)
            if left > 0:
                left -= 1
            else:
                left = 0

            if right == fixed:
                right -= 1

            continue

        left += 1
        right -= 1

    return True


print(almost_palindrome("raceacar"))
print(almost_palindrome("abccdba"))
print(almost_palindrome("abcdefdba"))
print(almost_palindrome(""))
print(almost_palindrome("a"))
print(almost_palindrome("ab"))
print(almost_palindrome("abc"))
print(almost_palindrome("abcertretertertcba"))
