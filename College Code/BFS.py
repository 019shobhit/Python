graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':['H','I'],
    'E':['F'],
    'F':[],
    'G':[],
    'H':[],
    'I':[],
}
def bfs(graph, start):
    visited = set()
    queue = []
    
    bfs_order = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return bfs_order


print("BFS:", bfs(graph, 'A'))