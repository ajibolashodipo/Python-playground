def shortestPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    visited = set(nodeA)

    # initialize queue
    queue = [[nodeA, 0]]

    while queue:
        node, distance = queue.pop(0)

        if node == nodeB:
            return distance

        # cycle through the neighbours. notice that here we are updating the visited set before adding, not after
        # removing

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append([neighbour, distance + 1])

    return -1


def buildGraph(edges):
    adjacencyList = {}
    for first, second in edges:

        if first not in adjacencyList:
            adjacencyList[first] = [second]

        else:
            adjacencyList[first].append(second)

        if second not in adjacencyList:
            adjacencyList[second] = [first]

        else:
            adjacencyList[second].append(first)

    return adjacencyList


# shortestPath(edges, nodeA, nodeB)