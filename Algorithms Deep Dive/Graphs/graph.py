class Graph:

    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        # check for existence
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []

        print(self.adjacencyList)

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


graph = Graph()
graph.addVertex("Tokyo")
graph.addVertex("Dallas")
graph.addVertex("Aspen")

graph.addEdge("Tokyo", "Dallas")
graph.addEdge("Dallas", "Aspen")

print(graph.adjacencyList)

graph.removeEdge("Tokyo", "Dallas")
graph.removeEdge("Dallas", "Aspen")
print(graph.adjacencyList)

graph.removeVertex("Tokyo")
print(graph.adjacencyList)