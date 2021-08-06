def countConstruct(target, wordBank):
    # extra space to accommodate for empty string (seed) and length of variable
    table = [0] * (len(target) + 1)
    table[0] = 1

    for i in range(len(table)):

        if table[i]:

            for word in wordBank:
                if target[i: i + len(word)] == word:
                    table[i + len(word)] += table[i]

    print(table)
    return table[len(target)]


print(countConstruct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))