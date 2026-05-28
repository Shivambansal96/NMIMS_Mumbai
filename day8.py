from collections import deque

class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

class Graph:
    def createEdges(self, graphList):

        for i in range(len(graphList)):
            graphList[i] = []

        graphList[0].append(Edge(0, 1))
        graphList[0].append(Edge(0, 2))

        graphList[1].append(Edge(1, 0))
        graphList[1].append(Edge(1, 2))

        graphList[2].append(Edge(2, 0))

    # # Directed Graph
    # def addEdges(self, graphList, src, dest):
    #     graphList[src].append(Edge(src, dest))

    # # UnDirected Graph
    def addEdges(self, graphList, src, dest):
        graphList[src].append(Edge(src, dest))
        graphList[dest].append(Edge(dest, src))

    def bfs(self, graphList):

        dq = deque()
        V = len(graphList)
        visited = [False] * V

        dq.append(0)

        while dq:
            vertex = dq.popleft()

            if visited[vertex] is False:
                print(vertex)
                visited[vertex] = True

            # for i in range(len(graphList[vertex])):
            #     # dq.append(graphList[vertex][i].dest)
            #     e = graphList[vertex][i]
            #     dq.append(e.dest)

            for i in graphList[vertex]:
                dq.append(i.dest)

graph = Graph()
# vertices = int(input("Enter number of Vertices: "))
vertices = 4
# noOfEdges = 6
graphList = [None] * vertices
# print(graphList)
# graph.createEdges(graphList)

for i in range(len(graphList)):
    graphList[i] = []

graph.addEdges(graphList, 0, 1)
graph.addEdges(graphList, 0, 2)
graph.addEdges(graphList, 1, 2)
graph.addEdges(graphList, 2, 3)

graph.bfs(graphList)

# graph.addEdges(graphList, 1, 0)

# graph.addEdges(graphList, 2, 1)
# graph.addEdges(graphList, 2, 0)



# print(graphList)
# print(graphList[0][0].src, graphList[0][0].dest)
# print(graphList[0][1].src, graphList[0][1].dest)

# for idx in graphList:
#     if len(idx) == 0:
#         continue

#     print(f"Paths of {idx[0].src} = ", end="")
#     for i in idx:
#         print(f"({i.src}, {i.dest})", end="")

#     print()





