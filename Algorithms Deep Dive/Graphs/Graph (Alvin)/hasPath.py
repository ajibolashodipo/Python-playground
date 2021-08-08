graph = {
    "f": ['g', 'i'],
    "g": ['h'],
    "h": [],
    "i": ['g', 'k'],
    "j": ['i'],
    "k": []
}


# dfs-recursive
def hasPath(graph, src, dest):
    if src == dest:
        return True

    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dest):
            return True

    return False


# bfs
def hasPath(graph, src, dest):
    queue = [src]

    while queue:

        popped = queue.pop(0)
        if popped == dest:
            return True

        for neighbour in graph[popped]:
            queue.append(neighbour)

    return False
