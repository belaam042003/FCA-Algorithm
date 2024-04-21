

from model.DeliveryModel import DeliveryModel
from view.DeliveryView import DeliveryView


class DeliveryController:
    def __init__(self, size, num_delivery_points, diffusion_rate=0.2):
        self.model = DeliveryModel(size, num_delivery_points, diffusion_rate)
        self.view = DeliveryView()

    def simulate_and_plot(self):
        self.model.simulate_delivery_routes()
        optimal_route = self.model.find_optimal_route()
        self.view.plot_route(self.model.graph, optimal_route)
