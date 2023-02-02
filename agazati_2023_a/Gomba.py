class Gomba:
    def __init__(self, sor):
        self.neve = sor[0]
        self.nemzettseg = sor[1]
        self.evszak = sor[2]

    def __str__(self):
        return f"{self.neve},{self.nemzettseg},{self.evszak}"