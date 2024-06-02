import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controller.graph_controller import GraphController
from model.graph import GraphModel
from view.graph_view import GraphView


import pandas as pd

class Main:
    def __init__(self, file_name):
        self.file_name = pd.read_csv(file_name)

    def run(self):
        dv_subset = self.file_name[0:5]

        # Crear el modelo
        graph_model = GraphModel(dv_subset)

        # Crear la vista
        graph_view = GraphView(graph_model.get_graph())

        # Crear el controlador
        graph_controller = GraphController(graph_model, graph_view)

        # Visualizar el grafo
        graph_controller.visualize_graph()

        # Encontrar el camino más corto
        graph_controller.find_shortest_path()


if __name__ == "__main__":
    file_name = "TeamRui/data/delivery_dataframe.csv"  
    main = Main(file_name)
    main.run()