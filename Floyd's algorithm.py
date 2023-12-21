Numberofvertices=6
Infinity=1000000000
def display(distance):
    for i in range(Numberofvertices):
        for j in range(Numberofvertices):
            if distance[i][j] == Infinity:
                print("Infinity", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")
def floyds(graph):
    distance = [list(row) for row in graph]
    for k in range(Numberofvertices):
        for i in range(Numberofvertices):
            for j in range(Numberofvertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    display(distance)
print("The shortest distances between every possible pair of vertices is:\n")
graph = [
    [0, 11, Infinity, 5, Infinity, 2],
    [4, 0, Infinity, 2, 1, Infinity],
    [Infinity, 7, 0, Infinity, 8, 1],
    [Infinity, Infinity, 9, 0, 3, 8],
    [Infinity, Infinity, 7, 9, 0, 6],
    [2, Infinity, 1, 8, 6, 0]
]
floyds(graph)
