# 3 leetcode- longest substring without repeating characters

# brute force
# time= O(n^2)
# space= O(n)

def repeating_substring(s):
    # edge cases
    if len(s) <= 1:
        return len(s)

    global_max = 0
    for i in range(len(s)):
        local_max = 0
        temp = ""  # or use a hashmap instead
        for j in range(i, len(s)):
            if s[j] not in temp:
                temp += s[j]
                local_max += 1
                global_max = max(local_max, global_max)
            else:
                break

    return global_max


# optimized solution
# time= O(n)
# space= O(n)
def repeating_substring1(s):
    # edge cases
    if len(s) <= 1:
        return len(s)

    # initialize pointers and hashmap
    left = 0
    largest = 0
    obj = {}

    for right in range(len(s)):
        currChar = s[right]
        # if current element exists in the dict, update it accordingly
        if currChar in obj:

            # store index of found character for subsequent access
            prevSeenIndex = obj[currChar]
            # then check if its index is within the current window
            if prevSeenIndex >= left:
                # slide the window to one element past the encountered element
                left = prevSeenIndex + 1

        # then update regardless. whether value was found in dict or not.
        # this makes sense because we either add a new entry to the dict or update an existing one.
        # either way, the update occurs, hence it stays outside the conditional
        else:
            obj[currChar] = right

        largest = max(largest, right - left + 1)

    return largest


print(repeating_substring("abcbdca"))
print(repeating_substring1("abcbdca"))
