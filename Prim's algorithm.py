Infinity=1000000000
Numberofvertices=6
G = [
    [0, 1, 3, 0, 1, 2],
    [1, 0, 2, 5, 4, 0],
    [3, 2, 0, 4, 7, 1],
    [0, 5, 4, 0, 9, 8],
    [0, 5, 7, 9, 0, 6],
    [2, 0, 1, 8, 6, 0]
]
selected=[False]*Numberofvertices
selected[0]=True
no_edge=0
print("Edge : Weight\n")
while no_edge < Numberofvertices-1:
    minimum=Infinity
    x = 0
    y = 0
    for i in range(Numberofvertices):
        if selected[i]:
            for j in range(Numberofvertices):
                if not selected[j] and G[i][j] and minimum > G[i][j]:
                    minimum = G[i][j]
                    x = i
                    y = j
    print(f"{x}-{y}:{G[x][y]}")
    selected[y] = True
    no_edge += 1
