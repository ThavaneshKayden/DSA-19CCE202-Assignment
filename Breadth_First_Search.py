from collections import deque #using functions to pop from the left
graph = {
    'X': ['Y', 'Z', 'W'],
    'Y': ['X'],
    'Z': ['X', 'W'],
    'W': ['X', 'Z', 'U'],
    'U': ['W'],
}
def breadth_first_search(start_node):
    visited = set()
    queue = deque([start_node])
    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)
            queue.extend(neigh for neigh in graph[current_node] if neigh not in visited)
breadth_first_search('X')
