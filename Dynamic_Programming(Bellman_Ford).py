class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.edges=[]
    def add_edge(self,u,v,weight):
        self.edges.append((u,v,weight))
    def bellman_ford(self,source):
        distances={vertex: float('inf') for vertex in range(self.vertices)}
        predecessors={vertex: None for vertex in range(self.vertices)}
        distances[source]=0
        for _ in range(self.vertices - 1):
            for u, v, weight in self.edges:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u
        for u, v, weight in self.edges:
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative cycle")
        return distances, predecessors
num_vertices = int(input("Enter the number of vertices: "))
graph = Graph(num_vertices)
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    u, v, weight = map(int, input("Enter edge (u v weight) format: ").split())
    graph.add_edge(u, v, weight)
source_vertex = int(input("Enter the source vertex: "))
distances, predecessors = graph.bellman_ford(source_vertex)
print(f"Shortest distances from source vertex {source_vertex}")
for vertex in range(graph.vertices):
    print(f"Vertex {vertex}: Distance = {distances[vertex]}, Predecessor = {predecessors[vertex]}")
