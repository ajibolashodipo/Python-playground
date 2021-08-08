def hasPath(graph, src, dest, visited={}):
    if src == dest:
        return True

    # check against cycle by checking visited dictionary
    if src in visited:
        return False

    # at this point, we know that node is not in the visited dict
    visited[src] = True

    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dest):
            return True

    return False


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


def undirectedPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)

    # find path from start to destination
    return hasPath(graph, nodeA, nodeB)


edges = [['i', 'j'], ['k', 'i'], ['m', 'k'], ['k', 'l'], ['o', 'n']]

print(undirectedPath(edges, "j", "m"))
