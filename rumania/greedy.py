import heapq

def greedy_search(G, heuristics, start, goal):
    frontier = []
    heapq.heappush(frontier, (heuristics[start], [start]))
    visited = set()

    while frontier:
        _, path = heapq.heappop(frontier)
        current = path[-1]
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for neighbor in G.neighbors(current):
            if neighbor not in visited:
                heapq.heappush(frontier, (heuristics[neighbor], path + [neighbor]))
    return None