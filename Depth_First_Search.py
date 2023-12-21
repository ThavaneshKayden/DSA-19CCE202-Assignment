class Graph:
    def __init__(self, graph_dictionary):
        self.graph = graph_dictionary
        self.visited = set()
    def depth_first_search(self, node):
        if node not in self.visited:
            print(node)
            self.visited.add(node)
            for neighbor in self.graph[node]:
                self.depth_first_search(neighbor)
graph_dictionary= {
    '6': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}
graph=Graph(graph_dictionary)
start_node = input("Enter the starting node for Depth First Search: ")
print(f"Starting Depth First Search from Node {start_node}:")
graph.depth_first_search(start_node)