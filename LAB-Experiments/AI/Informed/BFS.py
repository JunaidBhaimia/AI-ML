#BFS
from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.g = defaultdict(list)
    def addEdge(self, u, v):
        self.g[u].append(v)
    def BFS(self, s):
        visited, q = set([s]), deque([s])
        while q:
            v = q.popleft()
            print(v, end=" ")
            for i in self.g[v]:
                if i not in visited:
                    visited.add(i)
                    q.append(i)
g = Graph()
edges = [(0,1),(0,2),(1,2),(2,0),(2,3),(3,3)]
for u, v in edges:
    g.addEdge(u, v)
print("Following is Breadth First Traversal" " (starting from vertex 2)")
g.BFS(2)
