import networkx as nx

def get_romania_graph():
    G = nx.Graph()
    # Añade nodos y aristas con pesos (distancias)
    edges = [
        ("Arad", "Zerind", 75),
        ("Arad", "Sibiu", 140),
        ("Arad", "Timisoara", 118),
        ("Zerind", "Oradea", 71),
        ("Zerind", "Arad", 75),
        ("Oradea", "Sibiu", 151),
        ("Oradea", "Zerind", 71),
        ("Sibiu", "Fagaras", 99),
        ("Sibiu", "Rimnicu Vilcea", 80),
        ("Sibiu", "Oradea", 151),
        ("Sibiu", "Arad", 140),
        ("Timisoara", "Lugoj", 111),
        ("Timisoara", "Arad", 118),
        ("Lugoj", "Mehadia", 70),
        ("Lugoj", "Timisoara", 111),
        ("Mehadia", "Drobeta", 75),
        ("Mehadia", "Lugoj", 70),
        ("Drobeta", "Craiova", 120),
        ("Drobeta", "Mehadia", 75),
        ("Craiova", "Pitesti", 138),
        ("Craiova", "Rimnicu Vilcea", 146),
        ("Craiova", "Drobeta", 120),
        ("Rimnicu Vilcea", "Sibiu", 80),
        ("Rimnicu Vilcea", "Pitesti", 97),
        ("Rimnicu Vilcea", "Craiova", 146),
        ("Fagaras", "Sibiu", 99),
        ("Fagaras", "Bucharest", 211),
        ("Pitesti", "Rimnicu Vilcea", 97),
        ("Pitesti", "Craiova", 138),
        ("Pitesti", "Bucharest", 101),
        ("Bucharest", "Fagaras", 211),
        ("Bucharest", "Pitesti", 101),
        ("Bucharest", "Giurgiu", 90),
        ("Bucharest", "Urziceni", 85),
        ("Giurgiu", "Bucharest", 90),
        ("Urziceni", "Bucharest", 85),
        ("Urziceni", "Hirsova", 98),
        ("Urziceni", "Vaslui", 142),
        ("Hirsova", "Urziceni", 98),
        ("Hirsova", "Eforie", 86),
        ("Eforie", "Hirsova", 86),
        ("Vaslui", "Urziceni", 142),
        ("Vaslui", "Iasi", 92),
        ("Iasi", "Vaslui", 92),
        ("Iasi", "Neamt", 87),
        ("Neamt", "Iasi", 87)
    ]
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    # Posiciones aproximadas para visualización (puedes ajustar)
    positions = {
        "Arad": (0, 5), "Zerind": (-1, 7), "Oradea": (-2, 9), "Sibiu": (2, 8), "Timisoara": (-1, 3),
        "Lugoj": (0, 1), "Mehadia": (1, 0), "Drobeta": (3, -1), "Craiova": (6, -2), "Rimnicu Vilcea": (5, 6),
        "Fagaras": (7, 9), "Pitesti": (8, 4), "Bucharest": (12, 2), "Giurgiu": (13, 0), "Urziceni": (14, 4),
        "Hirsova": (17, 6), "Eforie": (19, 7), "Vaslui": (17, 2), "Iasi": (19, 0), "Neamt": (21, 1)
    }
    return G, positions

def get_heuristics():
    # Heurística: distancia en línea recta a Bucharest
    return {
        "Arad": 366, "Bucharest": 0, "Craiova": 160, "Drobeta": 242, "Eforie": 161,
        "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151, "Iasi": 226, "Lugoj": 244,
        "Mehadia": 241, "Neamt": 234, "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193,
        "Sibiu": 253, "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374
    }