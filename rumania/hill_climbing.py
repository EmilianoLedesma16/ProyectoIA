def hill_climbing(G, heuristics, start, goal):
    current = start
    path = [current]
    visited = set([current])

    while current != goal:
        neighbors = [n for n in G.neighbors(current) if n not in visited]
        if not neighbors:
            return None  # No hay camino
        # Selecciona el vecino con menor heurística (Hill Climbing)
        next_node = min(neighbors, key=lambda n: heuristics[n])
        if heuristics[next_node] >= heuristics[current]:
            return None  # No mejora, estancado
        path.append(next_node)
        visited.add(next_node)
        current = next_node
    return path