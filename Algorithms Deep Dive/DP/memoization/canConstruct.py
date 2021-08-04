def canConstruct(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
    # base case

    if target == "":
        return True

    for word in wordBank:
        # check that the word starts at the beginning of target
        if target.find(word) == 0:
            suffix = target[len(word):]

            # early return
            if canConstruct(suffix, wordBank, memo) is True:
                memo[target] = True
                return True
            
    memo[target] = False
    return False



