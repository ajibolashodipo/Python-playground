def allConstruct(target, wordBank):
    # extra space to accommodate for empty string (seed) and length of variable

    # BE CAREFUL ABOUT HOW YOU DEFINE A 2D ARRAY

    # WRONG
    # table = [[]] * (len(target) + 1)

    # CORRECT
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    print(table)
    for i in range(len(table)):

        for word in wordBank:
            if target[i: i + len(word)] == word:
                # maps through each subArray, spreads its content and adds the word into it
                newCombinations = list(map(lambda subArray: [*subArray, word], table[i]))

                # extend to the set of destination subarrays. extend is just glorified append btw
                table[i + len(word)].extend(newCombinations)

    return table[len(target)]


print(allConstruct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))
