import numpy as np

class MushroomOptimization:
    """
    Optimización de rutas utilizando un algoritmo inspirado en colonias de hongos.

    Attributes:
        graph (nx.DiGraph): Grafo en el que se realizará la optimización.
        num_mushrooms (int): Número de "hongos" (agentes) en la colonia.
        num_iterations (int): Número de iteraciones para la optimización.
    """
    
    def __init__(self, graph, num_mushrooms, num_iterations):
        """
        Inicializa una instancia de MushroomOptimization.

        Args:
            graph (nx.DiGraph): Grafo en el que se realizará la optimización.
            num_mushrooms (int): Número de "hongos" (agentes) en la colonia.
            num_iterations (int): Número de iteraciones para la optimización.
        """
        self.graph = graph  # Asigna el grafo proporcionado al atributo de instancia
        self.num_mushrooms = num_mushrooms  # Asigna el número de "hongos" al atributo de instancia
        self.num_iterations = num_iterations  # Asigna el número de iteraciones al atributo de instancia


    def run(self):
        """
        Ejecuta la optimización para encontrar el camino más corto.

        Returns:
            tuple: Camino más corto encontrado y su distancia.
        """
        all_time_shortest_path = ("placeholder", np.inf)  # Inicializa el camino más corto con un valor placeholder y distancia infinita
        for _ in range(self.num_iterations):  # Itera el número de veces especificado por num_iterations
            all_paths = self.construct_colony_paths()  # Construye los caminos para toda la colonia de hongos
            shortest_path = min(all_paths, key=lambda x: x[1])  # Encuentra el camino más corto en la iteración actual
            if shortest_path[1] < all_time_shortest_path[1]:  # Si el camino encontrado es más corto que el anterior
                all_time_shortest_path = shortest_path  # Actualiza el camino más corto
        return all_time_shortest_path  # Retorna el camino más corto encontrado


    def construct_colony_paths(self):
        """
        Construye los caminos para toda la colonia de hongos.

        Returns:
            list: Lista de caminos y sus distancias.
        """
        all_paths = []  # Inicializa una lista para almacenar todos los caminos
        for _ in range(self.num_mushrooms):  # Itera sobre el número de hongos
            path = self.construct_path(0)  # Construye un camino desde el nodo inicial (0)
            all_paths.append((path, self.path_distance(path)))  # Añade el camino y su distancia a la lista de todos los caminos
        return all_paths  # Retorna la lista de todos los caminos

    def construct_path(self, start):
        """
        Construye un camino a partir de un nodo inicial.

        Args:
            start (int): Nodo inicial.

        Returns:
            list: Lista de tuplas que representan el camino.
        """
        path = []  # Inicializa una lista para almacenar el camino
        visited = set()  # Inicializa un conjunto para rastrear los nodos visitados
        visited.add(start)  # Añade el nodo inicial al conjunto de visitados
        prev = start  # Establece el nodo inicial como el nodo previo
        for _ in range(len(self.graph.nodes) - 1):  # Itera sobre el número de nodos menos uno
            move = self.pick_move(list(self.graph[prev].keys()), visited)  # Selecciona el próximo movimiento
            path.append((prev, move))  # Añade el movimiento al camino
            prev = move  # Actualiza el nodo previo
            visited.add(move)  # Añade el nodo actual al conjunto de visitados
        return path  # Retorna el camino construido


    def pick_move(self, neighbors, visited):
        """
        Selecciona el próximo movimiento (nodo) de manera aleatoria.

        Args:
            neighbors (list): Lista de nodos vecinos.
            visited (set): Conjunto de nodos ya visitados.

        Returns:
            int: Nodo seleccionado para el próximo movimiento.
        """
        neighbors = [n for n in neighbors if n not in visited]  # Filtra los vecinos que no han sido visitados
        move = np.random.choice(neighbors)  # Selecciona aleatoriamente uno de los vecinos no visitados
        return move  # Retorna el nodo seleccionado

    def path_distance(self, path):
        """
        Calcula la distancia total de un camino.

        Args:
            path (list): Lista de tuplas que representan el camino.

        Returns:
            float: Distancia total del camino.
        """
        total_dist = 0  # Inicializa la distancia total a cero
        for ele in path:  # Itera sobre cada par de nodos en el camino
            total_dist += self.graph[ele[0]][ele[1]]['weight']  # Suma la distancia (peso) de cada arista al total
        return total_dist  # Retorna la distancia total del camino
