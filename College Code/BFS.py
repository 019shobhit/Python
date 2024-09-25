graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':['E'],
    'E':['G'],
    'F':[],
    'G':[]
}

visited=[]
stack=[]
def dfs(vistied,graph,node) : 
    visited.append(node)
    stack.append(node)
    while stack :
        s=stack.pop()
        print(s , end =" ")
        for neighbour in graph[s] :
           if neighbour not in visited:
              visited.append(neighbour)
              stack.append(neighbour)

dfs(visited,graph,'A')