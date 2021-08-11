def numberOfIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    count = 0

    # iterate through the grid
    for row in range(rows):
        for col in range(cols):

            if explore(grid, row, col, visited):
                count += 1
    print(visited)
    return count


def explore(grid, row, col, visited):
    # check for bounds
    if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1:
        return False

    # check for bounds (as done above) before checking for water cos row,col could be out of bounds

    # check for water
    if grid[row][col] == "W":
        return False

    # check for cycle detection
    if (row, col) in visited:
        return False

    # reaching this point means we have arrived upon unexplored land
    # add island to visited set
    visited.add((row, col))

    # explore in all 4 directions (DFS)
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for r, c in direction:
        explore(grid, row + r, col + c, visited)

    # getting to this point means we are done exploring a specific island
    return True


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(numberOfIslands(grid))
