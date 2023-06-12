
class Conta:
    def __init__(self, numero, nome, natureza):
        self.numero = numero
        self.nome = nome
        self.natureza = natureza
        self.saldo = 0

    def debitar(self, valor):
        self.saldo -= valor

    def creditar(self, valor):
        self.saldo += valor
