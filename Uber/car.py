from accountDriver import Driver
class Car():
    placa    = str
    modelo   = str
    color    = str
    año      = str
    
    def __init__(self, placa, modelo, color, año, Driver):
        self.placa  = placa
        self.modelo = modelo
        self.color  = color
        self.año    = año
        self.driver = Driver