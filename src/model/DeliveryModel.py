import numpy as np

class DeliveryModel:
    def __init__(self, size, num_delivery_points, diffusion_rate=0.2):
        self.size = size
        self.num_delivery_points = num_delivery_points
        self.diffusion_rate = diffusion_rate
        self.graph = None

    def simulate_delivery_routes(self):
        grid = np.zeros((self.size, self.size))

        for _ in range(self.num_delivery_points):
            x = np.random.randint(self.size)
            y = np.random.randint(self.size)
            grid[x, y] += 1

        for _ in range(self.num_delivery_points):
            new_grid = grid.copy()

            for i in range(1, self.size - 1):
                for j in range(1, self.size - 1):
                    neighbors_avg = (grid[i-1:i+2, j-1:j+2].sum() - grid[i, j]) / 8
                    new_grid[i, j] += self.diffusion_rate * neighbors_avg

            grid = new_grid

        self.graph = np.zeros((self.size ** 2, self.size ** 2))
        for i in range(self.size ** 2):
            for j in range(self.size ** 2):
                self.graph[i][j] = np.linalg.norm(np.array([i % self.size, i // self.size]) - np.array([j % self.size, j // self.size]))

    def find_optimal_route(self, start_node=0):
        num_nodes = len(self.graph)
        visited = [False] * num_nodes
        path = [start_node]
        visited[start_node] = True

        for _ in range(num_nodes - 1):
            min_distance = float('inf')
            nearest_node = None
            current_node = path[-1]

            for neighbor in range(num_nodes):
                if not visited[neighbor] and self.graph[current_node][neighbor] < min_distance:
                    min_distance = self.graph[current_node][neighbor]
                    nearest_node = neighbor

            path.append(nearest_node)
            visited[nearest_node] = True

        path.append(path[0])  # Agregar el nodo inicial al final del camino para cerrar el ciclo
        return path
