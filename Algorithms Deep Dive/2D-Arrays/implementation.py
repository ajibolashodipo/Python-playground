# initialize direction array. this can be modified accordingly. Here, we do in the order top,right,down, left
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def dfs(matrix, row, col, seen, values):
    # perform boundary checks
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col] is True:
        return

    # update values array
    values.append(matrix[row][col])
    seen[row][col] = True

    # loop through direction array. remember it is top,right,down,left
    for direc in direction:
        r, c = direc

        row = row + r
        col = col + c

        # recursive call
        dfs(matrix, row, col, seen, values)


def traversalDFS(matrix):
    # replicate 2d array of booleans
    row = [False] * len(matrix[0])
    seen = [row for _ in range(len(matrix))]

    # initialize values array
    values = []

    # make recursive calls
    startRow = 0
    startCol = 0
    dfs(matrix, startRow, startCol, seen, values)
