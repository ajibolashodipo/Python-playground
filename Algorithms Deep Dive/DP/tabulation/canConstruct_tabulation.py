def canConstruct(target, wordBank):
    table = [True] * (len(target) + 1)

    # set zeroth index to true
    table[0] = True

    for i in range(len(table)):
        if table[i] == True:

            # then iterate through the wordBank array
            for word in wordBank:

                # if the word matches the characters starting at position i. the extra space in the table
                # now makes sense cos of how slice works. this makes sense. try to understand
                if target[i: i + len(word)] == word:
                    table[i + len(word)] = True

    return table[len(target)]


print(canConstruct("ajibola", ["a", "jib", 'ola']))