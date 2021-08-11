def minimumIslandSize(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    smallest = rows * cols
    for row in range(rows):
        for col in range(cols):
            # recurse with the return value in mind
            size = explore(grid, row, col, visited)

            # first check is nuanced but necessary. cos we could
            # get an erroneous value of 0 at the first "W", which would be wrong
            if size>0 and size < smallest:
                smallest = size

    return smallest


def explore(grid, row, col, visited):
    # check for bounds
    if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1:
        return 0

    # check for bounds (as done above) before checking for water cos row,col could be out of bounds

    # check for water
    if grid[row][col] == "W":
        return 0

    # check for cycle detection
    if (row, col) in visited:
        return 0

    # reaching this point means we have arrived upon unexplored land
    # add island to visited set
    visited.add((row, col))

    # initialize current valid island node
    size = 1

    # explore in all 4 directions (DFS)
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for r, c in direction:
        size += explore(grid, row + r, col + c, visited)

    # getting to this point means we are done exploring a specific island
    return size


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimumIslandSize(grid))