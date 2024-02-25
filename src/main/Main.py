import sys
sys.path.append("..")  # Agregar el directorio padre al sys.path

from controller.Controller import Controller

if __name__ == "__main__":
    controlador = Controller()
    controlador.saludar()
