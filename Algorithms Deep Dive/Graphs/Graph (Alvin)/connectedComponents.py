graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}


def connectedComponentCount(graph):
    visited = {}
    count = 0

    # regular traversal through the nodes. this makes sense as it checks for clusters in the graph
    for node in graph:
        if explore(graph, node, visited):
            count += 1

    return count


def explore(graph, current, visited):
    if current in visited:
        return False

    visited[current] = True

    for neighbour in graph[current]:
        explore(graph, neighbour, visited)

    # getting to this point means the code is done traversing the current cluster
    return True


print(connectedComponentCount(graph))
