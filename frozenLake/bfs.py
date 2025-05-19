from collections import deque

def bfs(env, return_explored=False):
    start = env.start
    goal = env.goal
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)
    explored = []

    while queue:
        current, path = queue.popleft()
        explored.append(current)
        if env.is_goal(current):
            if return_explored:
                return path, explored
            return path
        for neighbor in env.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    if return_explored:
        return None, explored
    return None