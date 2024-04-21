
from controller import DeliveryController;


def main():
    size = 10
    num_delivery_points = 20
    diffusion_rate = 0.2

    controller = DeliveryController(size, num_delivery_points, diffusion_rate)
    controller.simulate_and_plot()

if __name__ == "__main__":
    main()
