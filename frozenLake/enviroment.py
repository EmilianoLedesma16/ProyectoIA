""" Definición del entorno FrozenLake como un tablero cuadriculado.
0 = espacio libre, 1 = agujero, 2 = inicio, 3 = meta """

class FrozenLakeEnv:
    def __init__(self, grid=None):
        # Tablero 4x4 por defecto
        self.default_4x4 = [
            [0, 0, 2, 1],
            [0, 1, 0, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 3]
        ]
        # Tablero 8x8 de ejemplo
        self.default_8x8 = [
            [2,0,0,0,0,1,0,0],
            [0,1,0,0,1,0,1,0],
            [0,0,0,1,0,0,1,0],
            [1,1,0,0,0,1,0,0],
            [0,0,1,1,0,0,1,0],
            [0,1,0,0,1,0,0,0],
            [0,0,1,0,0,1,1,0],
            [1,0,0,1,0,0,0,3]
        ]
        if grid is not None:
            self.grid = grid
        else:
            self.grid = self.default_4x4
        self.n = len(self.grid)
        self.m = len(self.grid[0])
        self.start = self.find_value(2)
        self.goal = self.find_value(3)

    def set_grid(self, grid):
        self.grid = grid
        self.n = len(self.grid)
        self.m = len(self.grid[0])
        self.start = self.find_value(2)
        self.goal = self.find_value(3)

    def find_value(self, value):
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == value:
                    return (i, j)
        return None

    def is_valid(self, pos):
        i, j = pos
        return 0 <= i < self.n and 0 <= j < self.m and self.grid[i][j] != 1

    def is_goal(self, pos):
        return pos == self.goal

    def get_neighbors(self, pos):
        i, j = pos
        moves = [(-1,0),(1,0),(0,-1),(0,1)]
        neighbors = []
        for di, dj in moves:
            ni, nj = i+di, j+dj
            if self.is_valid((ni, nj)):
                neighbors.append((ni, nj))
        return neighbors