import networkx as nx
import matplotlib.pyplot as plt

class GraphView:
    """
    Clase para visualizar un grafo y sus caminos más cortos.

    Attributes:
        graph (nx.Graph): El grafo que se va a visualizar.
    """
    
    def __init__(self, graph):
        """
        Inicializa una instancia de GraphView.

        Args:
            graph (nx.Graph): El grafo que se va a visualizar.
        """
        self.graph = graph  # Asigna el grafo proporcionado al atributo de la instancia

    def draw_graph(self):
        """
        Dibuja el grafo utilizando NetworkX y Matplotlib.
        """
        pos = nx.spring_layout(self.graph)  # Genera las posiciones de los nodos utilizando el algoritmo de layout por resorte
        nx.draw(self.graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")  # Dibuja los nodos y aristas del grafo con etiquetas y estilos personalizados
        labels = nx.get_edge_attributes(self.graph, 'weight')  # Obtiene las etiquetas de las aristas (los pesos)
        rounded_labels = {k: round(v, 1) for k, v in labels.items()}  # Redondea las etiquetas de las aristas a una cifra decimal
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=rounded_labels)  # Dibuja las etiquetas de las aristas en el grafo
        plt.title("Graph")  # Establece el título del grafo
        plt.show()  # Muestra el grafo

    def show_shortest_path(self, shortest_path):
        """
        Muestra el camino más corto en la consola.

        Args:
            shortest_path (tuple): El camino más corto y su distancia.
        """
        print("Shortest path:", shortest_path) # Imprime el camino más corto y su distancia en la consola

