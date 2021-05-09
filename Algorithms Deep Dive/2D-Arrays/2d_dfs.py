# initialize direction array. this can be modified accordingly. Here, we do in the order top,right,down, left
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]


# recursive function
def dfs(matrix, row, col, seen, values):
    # perform boundary and unique position checks
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col]:
        return

    # update values array
    values.append(matrix[row][col])
    seen[row][col] = True
    # print(row, col)
    # print(seen)

    # loop through direction array. remember it is top,right,down,left
    for direc in direction:
        print(direc)
        r, c = direc

        # recursive call
        dfs(matrix, row+r, col+c, seen, values)


def traversalDFS(matrix):
    # replicate 2d array of booleans
    cols = len(matrix[0])
    row = len(matrix)
    seen = [[False for i in range(cols)] for j in range(row)]

    # initialize values array
    values = []

    # make recursive calls starting with row=0, col=0
    startRow = 0
    startCol = 0
    dfs(matrix, startRow, startCol, seen, values)
    return values


testMatrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]

print(traversalDFS(testMatrix))
