def gridTraveller(m, n):
    rows = m + 1
    cols = n + 1
    grid = [[0 for i in range(cols)] for j in range(rows)]

    # initialize base case ish
    grid[1][1] = 1

    # iterate through the array and add val of current position to the position to the left and position to the bottom
    for row in range(rows):
        for col in range(cols):
            if (col + 1) < cols:
                grid[row][col + 1] += grid[row][col]
            if row + 1 < rows:
                grid[row + 1][col] += grid[row][col]

    # print(grid)


gridTraveller(3, 3)
