import networkx as nx
import numpy as np

class GraphModel:
    """
    Modelo de grafo que representa la red de entregas.

    Attributes:
        G (nx.DiGraph): Grafo dirigido que contiene nodos y aristas con información de entregas.
    """
        
    def __init__(self, dv_subset):
        """
        Inicializa una instancia de GraphModel.

        Args:
            dv_subset (DataFrame): Subconjunto de datos con información de entregas.
        """
        self.G = nx.DiGraph()  # Crea una instancia de un grafo dirigido de NetworkX
        self.construct_graph(dv_subset)  # Llama al método construct_graph para construir el grafo


    def construct_graph(self, dv_subset):
        """
        Construye el grafo a partir de un subconjunto de datos.

        Args:
            dv_subset (DataFrame): Subconjunto de datos con información de entregas.
        """
        for index, row in dv_subset.iterrows():
              # Añade un nodo al grafo para cada fila en dv_subset
            self.G.add_node(index,
                            delivery_time=round(row['DeliveryTime'], 1),  # Tiempo de entrega redondeado a una cifra decimal
                            packages=row['NumberPackagesDelivered'],  # Número de paquetes entregados
                            distance=round(row['DistanceToCityCenterFromDC'], 1),  # Distancia al centro de la ciudad redondeada a una cifra decimal
                            vehicle=row['VehicleType'],  # Tipo de vehículo
                            channel=row['FulfillmentChannel'])  # Canal de cumplimiento


        for i in range(len(dv_subset)):
            for j in range(len(dv_subset)):
                if i != j:
                    # Calcula la distancia absoluta entre dos nodos y añade una arista entre ellos con ese peso
                    distance = abs(dv_subset.at[i, 'DistanceToCityCenterFromDC'] - dv_subset.at[j, 'DistanceToCityCenterFromDC'])
                    self.G.add_edge(i, j, weight=round(distance, 1))  # Añade una arista con el peso de la distancia redondeada a una cifra decimal

    def get_graph(self):
        """
        Retorna el grafo construido.

        Returns:
            nx.DiGraph: Grafo dirigido con la información de entregas.
        """
        return self.G #Retorna el grafo dirigido

