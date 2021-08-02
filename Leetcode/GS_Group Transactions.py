def groupTransactions(transactions):
    txn = {}

    for i in transactions:
        if i in txn:
            txn[i] = txn[i] + 1

        else:
            txn[i] = 1

    lst = list(txn.items())
    b = sorted(lst, key=lambda x: (-x[1], x[0]))
    fin = []
    for word, freq in b:
        formString = word + ' ' + str(freq)
        fin.append(formString)
    print(fin)


# groupTransactions(['bin', 'can', 'bin', 'bin', 'apple'])


def segment(x, space):
    maxi = 0
    for index in range(len(space) - x + 1):
        mini = space[index]
        for j in range(index, index + x):
            mini = min(mini, space[j])
        maxi = max(maxi, mini)

    # print(maxi)
    return maxi


def segment(x, space):
    start =0
    j=0
    mini = space[0]
    maxi = 0
    for end, val in enumerate(space):
        mini= min(mini, space[end])

        if end-j +1==x:
            maxi= max(maxi,mini )
            start=0


    return maxi


segment(2, [8, 2, 4, 6])
