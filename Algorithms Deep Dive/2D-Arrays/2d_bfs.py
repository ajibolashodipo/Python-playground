# initialize direction array. this can be modified accordingly. Here, we do in the order top,right,down, left
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def traversalBFS(matrix):
    # initialize array of booleans to help us track which positions have been visited

    cols = len(matrix[0])
    row = len(matrix)
    seen = [[False for i in range(cols)] for j in range(row)]

    # initialize queue with first element in the array
    queue = [[0, 0]]

    values = []

    while queue:

        # pop first element from queue
        first = queue.pop(0)

        # destructure to get row and column
        row, col = first

        # check boundary and unique position conditions
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col] is True:
            continue

        # push value into values array
        values.append(matrix[row][col])

        # update seen array to true
        seen[row][col] = True

        # then add neighbouring elements to queue
        # loop through direction array. remember it is top,right,down,left
        for direc in direction:
            r, c = direc

            queue.append([row + r, col + c])

    return values


matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]

print(traversalBFS(matrix))
