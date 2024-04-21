import numpy as np
import matplotlib.pyplot as plt

def simulate_delivery_routes(size, num_delivery_points, diffusion_rate=0.2):
    grid = np.zeros((size, size))
    center = size // 2
    grid[center, center] = 1  # Start with a central point

    # Simulate diffusion of delivery routes
    for _ in range(num_delivery_points):
        x = np.random.randint(size)
        y = np.random.randint(size)
        grid[x, y] += 1

    for _ in range(num_delivery_points):
        new_grid = grid.copy()

        for i in range(1, size - 1):
            for j in range(1, size - 1):
                neighbors_avg = (grid[i-1:i+2, j-1:j+2].sum() - grid[i, j]) / 8
                new_grid[i, j] += diffusion_rate * neighbors_avg

        grid = new_grid

    return grid

def optimize_delivery_routes(graph, start=0):
    """
    Encuentra la ruta más corta utilizando el algoritmo del vecino más cercano.
    """
    num_nodes = len(graph)
    visited = [False] * num_nodes
    path = [start]
    visited[start] = True

    for _ in range(num_nodes - 1):
        min_distance = float('inf')
        nearest_node = None
        current_node = path[-1]

        for neighbor in range(num_nodes):
            if not visited[neighbor] and graph[current_node][neighbor] < min_distance:
                min_distance = graph[current_node][neighbor]
                nearest_node = neighbor

        path.append(nearest_node)
        visited[nearest_node] = True

    # Agregar el nodo inicial al final del camino para cerrar el ciclo
    path.append(path[0])
    return path

def plot_delivery_routes(grid):
    plt.imshow(grid, cmap='copper', interpolation='nearest')
    plt.colorbar(label='Route Intensity')
    plt.title('Delivery Routes Optimization')
    plt.show()

def plot_route(graph, route):
    """
    Visualiza la ruta en el gráfico.
    """
    plt.imshow(graph, cmap='copper', interpolation='nearest')
    plt.colorbar(label='Route Intensity')
    x = [p % len(graph) for p in route]
    y = [p // len(graph) for p in route]
    plt.plot(x, y, 'r-o')
    plt.title('Optimized Delivery Route')
    plt.show()

if __name__ == "__main__":
    # Parámetros de simulación
    size = 10
    num_delivery_points = 20
    diffusion_rate = 0.2

    # Simular la matriz de intensidad de la ruta
    delivery_grid = simulate_delivery_routes(size, num_delivery_points, diffusion_rate)

    # Convertir la matriz en un grafo ponderado (distancia euclidiana)
    graph = np.zeros((size ** 2, size ** 2))
    for i in range(size ** 2):
        for j in range(size ** 2):
            graph[i][j] = np.linalg.norm(np.array([i % size, i // size]) - np.array([j % size, j // size]))

    # Encontrar la ruta óptima utilizando el algoritmo del vecino más cercano
    optimal_route = optimize_delivery_routes(graph)

    # Visualizar la ruta óptima
    plot_route(delivery_grid, optimal_route)
