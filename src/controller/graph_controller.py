from model.mushroom_class import MushroomOptimization


class GraphController:
    """
    Controlador para manejar la interacción entre el modelo de grafo y la vista.

    Attributes:
        model (GraphModel): El modelo de grafo que contiene la lógica de datos.
        view (GraphView): La vista que maneja la visualización del grafo.
    """

    def __init__(self, model, view):
        """
        Inicializa una instancia de GraphController.

        Args:
            model (GraphModel): El modelo de grafo que contiene la lógica de datos.
            view (GraphView): La vista que maneja la visualización del grafo.
        """
        self.model = model
        self.view = view

    def visualize_graph(self):
        """
        Visualiza el grafo utilizando la vista.
        """
        self.view.draw_graph()

    def find_shortest_path(self):
        """
        Encuentra y muestra el camino más corto utilizando la optimización de hongos.
        """
        # Inicializa el algoritmo de optimización de hongos con el grafo del modelo
        shortest_path_algo = MushroomOptimization(self.model.get_graph(), num_mushrooms=10, num_iterations=100)
        
        # Ejecuta el algoritmo para encontrar el camino más corto
        shortest_path = shortest_path_algo.run()
        
        # Muestra el camino más corto utilizando la vista
        self.view.show_shortest_path(shortest_path)
