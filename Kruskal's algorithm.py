def Kruskal(graph):
    edges = [(weight, u, v) for u, neighbors in graph.items() for v, weight in neighbors.items()]
    edges.sort()
    parent = {node: node for node in graph}
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]
    def union(u, v):
        root_u, root_v = find(u), find(v)
        parent[root_u] = root_v
    minimumspantree = []
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            minimumspantree.append((weight, u, v))
    return minimumspantree
inputg={
        'A': {'B': 5, 'D': 3},
        'B': {'A': 5, 'C': 7, 'D': 6},
        'C': {'B': 3, 'D': 9},
        'D': {'A': 3, 'B': 6, 'C': 8}
}
MST= Kruskal(inputg)
print("Minimum Spanning Tree (Kruskal's Algorithm):", MST)


