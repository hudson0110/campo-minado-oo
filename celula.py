class Celula:
    def __init__(self):
        self.bomba = False  # Indica se a célula contém uma bomba
        self.revelada = False  # Indica se a célula foi revelada
        self.marcada = False  # Indica se a célula foi marcada com uma bandeira
        self.numero = 0  # Número de bombas adjacentes

    def __repr__(self):
        return f"{'B' if self.bomba else self.numero}"