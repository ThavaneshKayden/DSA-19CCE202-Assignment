
infinity=1000000000
class Graph():
    def __init__(self, vertex):
        self.V = vertex
        self.graph = [[0 for column in range(vertex)] for row in range(vertex)]
    def printing(self, dist):
        print ("Vertex :\tDistance from Source")
        for node in range(self.V):
            print (node, "\t", "-->","\t",dist[node], "\n")
    def minDistance(self, dist, sptSet):
        min=infinity
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
        return min_index
    def dijkstra(self, src):
        distance = [infinity] * self.V
        distance[src] = 0
        count = [False] * self.V
        for i in range(self.V):
            x = self.minDistance(distance, count)
            count[x] = True
            for y in range(self.V):
                if self.graph[x][y] > 0 and count[y] == False and \
                distance[y] > distance[x] + self.graph[x][y]:
                        distance[y] = distance[x] + self.graph[x][y]
        self.printing(distance)
graph1 = Graph(6)
graph1.graph = [[0, 2, 5, 0, 1, 0],
            [9, 0, 0, 9, 7, 5],
            [5, 11, 0, 0, 3, 0],
            [0, 6, 0, 0, 3, 4],
            [7, 7, 3, 13, 0, 6],
            [0, 9, 0, 1, 4, 0]]
print("Distance-where our source is Node:2")
graph1.dijkstra(2)
print("Distance-where our source is Node:5")
graph1.dijkstra(5)



