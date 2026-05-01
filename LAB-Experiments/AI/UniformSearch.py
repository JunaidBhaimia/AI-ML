#Uniform search
import heapq
def ucs(graph, start, goal):
    pq = [(0, start)]   # (cost, node)
    visited = set()
    while pq:
        cost, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        print(f"Visited: {node} with cost {cost}")
        if node == goal:
            print("Goal reached with minimum cost:", cost)
            return
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor))
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
ucs(graph, 'A', 'F')
