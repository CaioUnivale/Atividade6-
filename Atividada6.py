class Motor:
    def ligar(self):
        print("Motor ligado")

class Roda:
    def girar(self):
        print("Roda girando")

class TanqueCombustivel:
    def encher(self):
        print("Tanque cheio")

class Carro:
    def __init__(self):
        self.motor = Motor()
        self.roda_dianteira_esquerda = Roda()
        self.roda_dianteira_direita = Roda()
        self.roda_traseira_esquerda = Roda()
        self.roda_traseira_direita = Roda()
        self.tanque = TanqueCombustivel()

    def ligar(self):
        print("Ligando o carro...")
        self.motor.ligar()

    def andar(self):
        print("O carro está andando...")
        for roda in [self.roda_dianteira_esquerda, self.roda_dianteira_direita, self.roda_traseira_esquerda, self.roda_traseira_direita]:
            roda.girar()

carro = Carro()
carro.ligar()
carro.andar()
carro.tanque.encher()