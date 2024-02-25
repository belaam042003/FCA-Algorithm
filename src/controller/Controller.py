from model.Model import Model
from view.View import View



class Controller:
    def __init__(self):
        self.modelo = Model()
        self.vista = View()

    def saludar(self):
        saludo = self.modelo.obtener_saludo()
        self.vista.mostrar_saludo(saludo)

if __name__ == "__main__":
    controlador = Controller()
    controlador.saludar()