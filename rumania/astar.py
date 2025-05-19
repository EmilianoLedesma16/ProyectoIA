import heapq

def astar_search(G, heuristics, start, goal):
    frontier = []
    heapq.heappush(frontier, (heuristics[start], 0, [start]))
    visited = set()

    while frontier:
        est_total, cost_so_far, path = heapq.heappop(frontier)
        current = path[-1]
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for neighbor in G.neighbors(current):
            if neighbor not in visited:
                edge_weight = G[current][neighbor]['weight']
                new_cost = cost_so_far + edge_weight
                est = new_cost + heuristics[neighbor]
                heapq.heappush(frontier, (est, new_cost, path + [neighbor]))
    return None