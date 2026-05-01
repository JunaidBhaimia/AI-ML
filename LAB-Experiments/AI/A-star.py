#A*
import heapq
def astar(graph, heuristic, start, goal):
    pq = [(0, start)]   # (f(n), node)
    g_cost = {start: 0}
    parent = {start: None}
    while pq:
        f, node = heapq.heappop(pq)
        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1], g_cost[goal]
        for neighbor, weight in graph[node]:
            new_g = g_cost[node] + weight
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic[neighbor]
                heapq.heappush(pq, (f_cost, neighbor))
                parent[neighbor] = node
    return None, float("inf")
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}
heuristic = {
    'A': 6, 'B': 4, 'C': 4,
    'D': 2, 'E': 1, 'F': 0
}
path, cost = astar(graph, heuristic, 'A', 'F')
print("Path:", path)
print("Cost:", cost)
