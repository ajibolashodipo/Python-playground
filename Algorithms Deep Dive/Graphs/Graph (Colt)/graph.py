class Graph:

    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        # check for existence
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []

        # print(self.adjacencyList)

    def addEdge(self, vertex1, vertex2):

        if vertex1 in self.adjacencyList:
            self.adjacencyList[vertex1].append(vertex2)
        if vertex2 in self.adjacencyList:
            self.adjacencyList[vertex2].append(vertex1)

    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.adjacencyList:
            self.adjacencyList[vertex1] = list(filter(lambda v: v != vertex2, self.adjacencyList[vertex1]))
        if vertex2 in self.adjacencyList:
            self.adjacencyList[vertex2] = list(filter(lambda v: v != vertex1, self.adjacencyList[vertex2]))

    def removeVertex(self, vertex):
        for v in self.adjacencyList[vertex]:
            self.removeEdge(v, vertex)

        # then delete the key itself
        del self.adjacencyList[vertex]

    def dfsRecursive(self, start):
        # create a list to store the end result
        result = []
        visited = {}

        def dfs(vertex):
            # checks if node is empty: empty graph
            if not vertex:
                return None

            # add vertex to result and add vertex to visited
            visited[vertex] = True
            # print(visited)
            result.append(vertex)

            for neighbour in self.adjacencyList[vertex]:
                # print("adetutu")
                print(neighbour)
                # if neighbour has not been visited
                if neighbour not in visited:
                    # print("ajibola")
                    # print(neighbour)
                    return dfs(neighbour)

        dfs(start)
        print(result)
        return result

    def dfsIterative(self, start):
        stack = [start]
        result = []
        visited = {}

        visited[start] = True
        while len(stack):
            # pop from stack
            currentVertex = stack.pop()
            result.append(currentVertex)

            # then we go to each of the popped element's neighbours'
            for neighbour in self.adjacencyList[currentVertex]:
                if neighbour not in visited:
                    visited[neighbour] = True
                    stack.append(neighbour)
        print(result)
        return result

    def bfs(self, start):
        result = []
        visited = {}
        queue = [start]

        visited[start] = True

        while queue:
            currentVertex = queue.pop(0)

            # push into results array
            result.append(currentVertex)

            # then loop through the array of current vertex
            for neighbour in self.adjacencyList[currentVertex]:

                if neighbour not in visited:
                    visited[neighbour] = True
                    queue.append(neighbour)

        print(result)
        return result


# graph = Graph()
# graph.addVertex("Tokyo")
# graph.addVertex("Dallas")
# graph.addVertex("Aspen")
#
# graph.addEdge("Tokyo", "Dallas")
# graph.addEdge("Dallas", "Aspen")
#
# print(graph.adjacencyList)
#
# graph.removeEdge("Tokyo", "Dallas")
# graph.removeEdge("Dallas", "Aspen")
# print(graph.adjacencyList)
#
# graph.removeVertex("Tokyo")
# print(graph.adjacencyList)

g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")

g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "E")
g.addEdge("D", "E")
g.addEdge("D", "F")
g.addEdge("E", "F")
g.dfsRecursive("A")
g.dfsIterative("A")
g.bfs("A")
# print("adj list")
# print(g.adjacencyList)
