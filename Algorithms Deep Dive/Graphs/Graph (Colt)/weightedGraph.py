class WeightedGraph:

    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        # check for existence
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []

        # print(self.adjacencyList)

    def addEdge(self, vertex1, vertex2, weight):

        if vertex1 in self.adjacencyList:
            self.adjacencyList[vertex1].append({"node": vertex2, "weight": weight})
        if vertex2 in self.adjacencyList:
            self.adjacencyList[vertex2].append({"node": vertex1, "weight": weight})


weighted = WeightedGraph()

weighted.addVertex("A")
weighted.addVertex("B")
weighted.addVertex("C")

weighted.addEdge("A", "B", 9)
weighted.addEdge("A", "C", 5)

print(weighted.adjacencyList)