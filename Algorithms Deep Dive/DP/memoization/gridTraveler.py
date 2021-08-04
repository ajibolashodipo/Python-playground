def gridTraveler(m, n, memo={}):
    # check if arguments are  in the memo
    key = str(m) + "," + str(n)
    if key in memo:
        return memo[key]

    # base cases (trivial and invalid)
    # trivial grid
    if m == 1 and n == 1:
        return 1

    # invalid grid
    if m == 0 or n == 0:
        return 0

    # recursive case. store key in memo
    memo[key] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)
    return memo[key]


print(gridTraveler(18, 18))
