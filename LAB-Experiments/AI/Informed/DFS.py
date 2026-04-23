#DFS
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
visited = set()          
traversal_order = []      
def dfs(node):
    if node not in visited:
        visited.add(node)                
        traversal_order.append(node)     

        for neighbor in graph[node]:  
            dfs(neighbor)
dfs('A')
print("\nFinal Traversal Order:")
print(" → ".join(traversal_order))
