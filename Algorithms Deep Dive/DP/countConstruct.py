def countConstruct(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1

    totalCount = 0
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            numWaysForRest = countConstruct(suffix, wordBank, memo)
            totalCount += numWaysForRest

    memo[target] = totalCount
    return totalCount


print(countConstruct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))
